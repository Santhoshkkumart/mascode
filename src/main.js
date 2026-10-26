const { app, BrowserWindow, ipcMain, shell } = require('electron');
const { spawn } = require('node:child_process');
const os = require('node:os');
const fs = require('node:fs/promises');
const path = require('node:path');
const solutionsDir = path.join(__dirname, 'solutions');
const solutionIndex = require(path.join(solutionsDir, 'index.json'));
const solutionById = new Map(solutionIndex.map(item => [item.id, item]));
function createWindow() {
  const win = new BrowserWindow({
    width: 1440, height: 920, minWidth: 1050, minHeight: 700,
    backgroundColor: '#0d1117',
    webPreferences: { preload: path.join(__dirname, 'preload.js'), contextIsolation: true, nodeIntegration: false }
  });
  win.loadFile(path.join(__dirname, 'index.html'));
}

function run(command, args, opts = {}) {
  return new Promise((resolve) => {
    const startedAt = process.hrtime.bigint();
    const elapsed = () => Number(process.hrtime.bigint() - startedAt) / 1e6;
    let stdout = '', stderr = '', timedOut = false;
    const child = spawn(command, args, { cwd: opts.cwd, windowsHide: true, shell: false, env: { ...process.env, ...opts.env } });
    const timer = setTimeout(() => { timedOut = true; child.kill('SIGKILL'); }, opts.timeout || 12000);
    child.stdout.on('data', d => { stdout += d; if (stdout.length > 100000) child.kill('SIGKILL'); });
    child.stderr.on('data', d => { stderr += d; if (stderr.length > 100000) child.kill('SIGKILL'); });
    if (opts.input) child.stdin.write(opts.input);
    child.stdin.end();
    child.on('error', e => { clearTimeout(timer); resolve({ code: -1, stdout, stderr: e.message, elapsedMs: elapsed() }); });
    child.on('close', code => { clearTimeout(timer); resolve({ code, stdout, stderr, timedOut, elapsedMs: elapsed() }); });
  });
}

ipcMain.handle('system-info', () => ({
  platform: `${os.type()} ${os.release()}`, arch: os.arch(), cores: os.cpus().length,
  cpu: os.cpus()[0]?.model || 'Unknown CPU', memory: os.totalmem(),
  appVersion: app.getVersion()
}));

ipcMain.handle('solutions-list', () => solutionIndex.map(({ id, title, topic, difficulty, starter, testCount, statement, examples, constraints, pattern, problemUrl, leetcodeId }) => ({ id, title, topic, difficulty, starter, testCount, statement, examples, constraints, pattern, problemUrl, leetcodeId })));
ipcMain.handle('solution-read', async (_event, id) => {
  const item = solutionById.get(id);
  if (!item) throw new Error('Unknown solution.');
  return fs.readFile(path.join(solutionsDir, item.path), 'utf8');
});
ipcMain.handle('tests-read', async (_event, id) => {
  const item = solutionById.get(id);
  if (!item) throw new Error('Unknown problem.');
  return fs.readFile(path.join(solutionsDir, item.testPath), 'utf8');
});
ipcMain.handle('run-problem-tests', async (_event, { id, code }) => {
  const item = solutionById.get(id);
  if (!item) return { code: -1, stdout: '', stderr: 'Unknown problem.', phase: 'test' };
  if (typeof code !== 'string' || code.length > 50000) return { code: -1, stdout: '', stderr: 'Code must be under 50 KB.', phase: 'test' };
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), 'mascode-tests-'));
  const problemDir = path.join(dir, 'problems', path.dirname(item.path));
  const testsSource = path.join(solutionsDir, item.testPath);
  const solutionPath = path.join(problemDir, 'solution.py');
  const testPath = path.join(problemDir, 'test_solution.py');
  const harnessPath = path.join(dir, 'run_tests.py');
  const harness = `import importlib.util, pathlib, traceback, sys\n\np = pathlib.Path(${JSON.stringify(testPath)})\nspec = importlib.util.spec_from_file_location('_mascode_tests', p)\nmod = importlib.util.module_from_spec(spec)\nspec.loader.exec_module(mod)\nnames = ${JSON.stringify(item.testNames)}\nfailed = 0\nfor name in names:\n    try:\n        getattr(mod, name)()\n        print('PASS|' + name)\n    except Exception as exc:\n        failed += 1\n        print('FAIL|' + name + '|' + type(exc).__name__ + ': ' + str(exc))\n        traceback.print_exc()\nprint(f'RESULT|{len(names)-failed}|{failed}|{len(names)}')\nsys.exit(1 if failed else 0)\n`;
  try {
    await fs.mkdir(problemDir, { recursive: true });
    await fs.writeFile(solutionPath, code, 'utf8');
    await fs.copyFile(testsSource, testPath);
    await fs.cp(path.join(solutionsDir, 'lib'), path.join(dir, 'lib'), { recursive: true });
    await fs.writeFile(harnessPath, harness, 'utf8');
    const command = process.platform === 'win32' ? 'python' : 'python3';
    const result = await run(command, ['-B', harnessPath], { cwd: dir, timeout: 20000, env: { PYTHONDONTWRITEBYTECODE: '1' } });
    if (result.code === -1 && result.stderr.includes('ENOENT')) result.stderr = `Python runtime not found: ${command}. Install Python 3 and restart MasCode.`;
    return { ...result, phase: 'test' };
  } finally { await fs.rm(dir, { recursive: true, force: true }); }
});

ipcMain.handle('compile-run', async (_event, { language, code, input = '' }) => {
  if (typeof code !== 'string' || code.length > 50000) return { code: -1, stdout: '', stderr: 'Code must be under 50 KB.' };
  if (typeof input !== 'string' || input.length > 50000) return { code: -1, stdout: '', stderr: 'Input must be under 50 KB.' };
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), 'local-code-lab-'));
  const file = async (name, data) => fs.writeFile(path.join(dir, name), data, 'utf8');
  try {
    let command, args;
    if (language === 'python') {
      await file('main.py', code); command = process.platform === 'win32' ? 'python' : 'python3'; args = ['main.py'];
    } else if (language === 'cpp') {
      await file('main.cpp', code);
      const build = await run('g++', ['-std=c++17', '-O2', 'main.cpp', '-o', 'main'], { cwd: dir, timeout: 20000 });
      if (build.code !== 0) return { ...build, phase: 'compile' };
      command = process.platform === 'win32' ? '.\\main.exe' : './main'; args = [];
    } else if (language === 'java') {
      await file('Main.java', code);
      const build = await run('javac', ['Main.java'], { cwd: dir, timeout: 20000 });
      if (build.code !== 0) return { ...build, phase: 'compile' };
      command = 'java'; args = ['-cp', dir, 'Main'];
    } else return { code: -1, stdout: '', stderr: 'Unsupported language.' };
    const result = await run(command, args, { cwd: dir, timeout: 12000, input });
    if (result.code === -1 && result.stderr.includes('ENOENT')) result.stderr = `Required runtime not found: ${command}. Install it and restart the app.`;
    return { ...result, phase: 'run' };
  } finally { await fs.rm(dir, { recursive: true, force: true }); }
});

ipcMain.handle('check-syntax', async (_event, { language, code }) => {
  if (typeof code !== 'string' || code.length > 50000) return { code: -1, stdout: '', stderr: 'Code must be under 50 KB.' };
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), 'mascode-check-'));
  try {
    let command, args, file;
    if (language === 'python') {
      file = 'main.py'; command = process.platform === 'win32' ? 'python' : 'python3'; args = ['-m', 'py_compile', file];
    } else if (language === 'cpp') {
      file = 'main.cpp'; command = 'g++'; args = ['-std=c++17', '-fsyntax-only', file];
    } else if (language === 'java') {
      file = 'Main.java'; command = 'javac'; args = ['-proc:none', file];
    } else return { code: -1, stdout: '', stderr: 'Unsupported language.' };
    await fs.writeFile(path.join(dir, file), code, 'utf8');
    const result = await run(command, args, { cwd: dir, timeout: 8000, env: { PYTHONDONTWRITEBYTECODE: '1' } });
    if (result.code === -1 && result.stderr.includes('ENOENT')) return { ...result, stderr: `${command} was not found on PATH.` };
    return result;
  } finally { await fs.rm(dir, { recursive: true, force: true }); }
});

ipcMain.handle('open-external', (_event, url) => {
  if (typeof url === 'string' && /^https:\/\//.test(url)) return shell.openExternal(url);
});

app.whenReady().then(() => { createWindow(); app.on('activate', () => { if (BrowserWindow.getAllWindows().length === 0) createWindow(); }); });
app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit(); });
