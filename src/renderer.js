const editor = CodeMirror.fromTextArea(document.getElementById('editor'), {
  value: '', mode: 'python', theme: 'default', lineNumbers: true, indentUnit: 4, tabSize: 4,
  indentWithTabs: false, smartIndent: true, electricChars: true,
  gutters: ['CodeMirror-linenumbers', 'CodeMirror-lintgutter'],
  extraKeys: {
    Enter: 'newlineAndIndent',
    Tab: cm => cm.replaceSelection('    ', 'end')
  }
});
const language = document.getElementById('language');
const status = document.getElementById('runStatus');
const selector = document.getElementById('problemSelect'), search = document.getElementById('problemSearch');
let problems = [], currentProblem = null, answerVisible = false, testsVisible = false, activeLanguage = 'python';
const drafts = new Map();
const draftKey = (problem, lang) => `${problem.id}:${lang}`;
let diagnosticMarks = [], syntaxCheckTimer = null, syntaxRequestId = 0;
const storageRead = (key, fallback) => { try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; } };
const storageWrite = (key, value) => { try { localStorage.setItem(key, JSON.stringify(value)); } catch {} };
let progress = storageRead('mascode-progress-v1', { solved: [], days: [] });
let profile = storageRead('mascode-profile-v1', { name: 'MasCode User', handle: 'mascode-user', email: '', bio: '' });
let complexityByProblem = storageRead('mascode-complexity-v1', {});
if (!Array.isArray(progress.solved)) progress.solved = [];
if (!Array.isArray(progress.days)) progress.days = [];

function clearDiagnostics() {
  diagnosticMarks.forEach(mark => mark.clear()); diagnosticMarks = [];
  for (let line = 0; line < editor.lineCount(); line++) {
    editor.removeLineClass(line, 'background', 'cm-error-line');
    editor.setGutterMarker(line, 'CodeMirror-lintgutter', null);
  }
}
function showDiagnostics(items) {
  clearDiagnostics();
  for (const item of items) {
    const line = Math.max(0, Math.min(editor.lineCount() - 1, item.line - 1));
    const text = editor.getLine(line) || ' ';
    editor.addLineClass(line, 'background', 'cm-error-line');
    const marker = document.createElement('div'); marker.className = 'cm-error-gutter'; marker.title = item.message; marker.textContent = '●';
    editor.setGutterMarker(line, 'CodeMirror-lintgutter', marker);
    diagnosticMarks.push(editor.markText({line, ch: 0}, {line, ch: Math.max(text.length, 1)}, {className: 'cm-error-underline', title: item.message}));
  }
}
function diagnosticsFrom(message, lang) {
  if (!message) return [];
  const found = [];
  if (lang === 'cpp') {
    for (const m of message.matchAll(/(?:main\.cpp|\.\/main\.cpp):(\d+):(\d+):\s*(?:fatal )?error:\s*(.*)/g)) found.push({line:Number(m[1]),message:m[3]});
  } else if (lang === 'java') {
    for (const m of message.matchAll(/Main\.java:(\d+):\s*error:\s*(.*)/g)) found.push({line:Number(m[1]),message:m[2]});
    for (const m of message.matchAll(/at Main\.[^(]+\(Main\.java:(\d+)\)/g)) found.push({line:Number(m[1]),message:'Runtime exception on this line'});
  } else {
    const pyLines = [...message.matchAll(/File ["'][^"']*(?:main|solution)\.py["'], line (\d+)/g)];
    if (pyLines.length) {
      const line = Number(pyLines[pyLines.length - 1][1]);
      const error = message.match(/(SyntaxError|IndentationError|NameError|TypeError|ValueError): (.*)/);
      found.push({line,message:error ? `${error[1]}: ${error[2]}` : 'Python error on this line'});
    }
  }
  return found;
}
function currentDraftKey() { return currentProblem ? draftKey(currentProblem, activeLanguage) : null; }
function saveDraft() { const key = currentDraftKey(); if (key) drafts.set(key, editor.getValue()); }
function saveComplexity() {
  if (!currentProblem) return;
  complexityByProblem[currentProblem.id]={time:document.getElementById('timeComplexity').value,space:document.getElementById('spaceComplexity').value};
  storageWrite('mascode-complexity-v1',complexityByProblem);
}
function setStarter() {
  if (!currentProblem) return;
  activeLanguage = language.value;
  const key = draftKey(currentProblem, activeLanguage);
  editor.setOption('mode', language.value === 'cpp' ? 'text/x-c++src' : language.value === 'java' ? 'text/x-java' : 'python');
  if (drafts.has(key)) editor.setValue(drafts.get(key));
  else editor.setValue(language.value === 'python' ? currentProblem.starter : '');
  clearDiagnostics();
}
function updateTestAvailability() {
  const python = language.value === 'python';
  document.getElementById('runTestsBtn').disabled = !python || !currentProblem;
  document.getElementById('submitBtn').disabled = !python || !currentProblem;
  document.getElementById('runHint').textContent = python ? 'Enter auto-indent · Tab = 4 spaces · Python tests' : 'Enter auto-indent · Tab = 4 spaces';
}
function renderQuestion(problem) {
  const body = document.getElementById('questionBody'); body.replaceChildren();
  if (!problem) return;
  const meta = document.createElement('div'); meta.className = 'question-meta';
  meta.textContent = `LeetCode #${problem.leetcodeId || '—'} · ${problem.topic}${problem.pattern ? ` · ${problem.pattern}` : ''}`;
  body.append(meta);
  const intro = document.createElement('section'); intro.className = 'question-intro';
  const heading = document.createElement('h3'); heading.textContent = 'Problem'; body.append(heading);
  const statement = document.createElement('p'); statement.className = 'question-statement'; statement.textContent = problem.statement; intro.append(heading, statement); body.append(intro);
  const examplesSection = document.createElement('section'); examplesSection.className = 'question-examples';
  const examplesTitle = document.createElement('h3'); examplesTitle.textContent = 'Examples'; examplesSection.append(examplesTitle);
  const examplesGrid = document.createElement('div'); examplesGrid.className = 'question-example-grid';
  for (const example of problem.examples || []) {
    const card = document.createElement('div'); card.className = 'question-example';
    const label = document.createElement('b'); label.textContent = example.label;
    const sample = document.createElement('pre'); sample.textContent = example.body;
    card.append(label, sample); examplesGrid.append(card);
  }
  examplesSection.append(examplesGrid); body.append(examplesSection);
  if (problem.constraints?.length) {
    const constraintsSection = document.createElement('section'); constraintsSection.className = 'question-constraints';
    const constraintsTitle = document.createElement('h3'); constraintsTitle.textContent = 'Constraints'; body.append(constraintsTitle);
    const list = document.createElement('ul');
    for (const constraint of problem.constraints) { const item = document.createElement('li'); item.textContent = constraint; list.append(item); }
    constraintsSection.append(constraintsTitle, list); body.append(constraintsSection);
  }
}

function dateKey(date = new Date()) {
  return `${date.getFullYear()}-${String(date.getMonth()+1).padStart(2,'0')}-${String(date.getDate()).padStart(2,'0')}`;
}
function shiftDay(key, amount) {
  const [y,m,d] = key.split('-').map(Number);
  const date = new Date(Date.UTC(y,m-1,d+amount));
  return `${date.getUTCFullYear()}-${String(date.getUTCMonth()+1).padStart(2,'0')}-${String(date.getUTCDate()).padStart(2,'0')}`;
}
function streakStats() {
  const days = new Set(progress.days), today = dateKey();
  let current = 0, cursor = days.has(today) ? today : days.has(shiftDay(today,-1)) ? shiftDay(today,-1) : null;
  while (cursor && days.has(cursor)) { current++; cursor = shiftDay(cursor,-1); }
  const sorted = [...days].sort(); let longest = 0, run = 0, previous = null;
  for (const day of sorted) { run = previous && shiftDay(previous,1) === day ? run + 1 : 1; longest = Math.max(longest,run); previous = day; }
  return { current, longest, activeDays: days.size };
}
function renderHeatmap(element) {
  element.replaceChildren();
  const days = new Set(progress.days), today = dateKey(), start = shiftDay(today,-48);
  for (let i=0;i<49;i++) {
    const key = shiftDay(start,i), cell = document.createElement('i');
    cell.className = `heat-cell${days.has(key) ? ' active' : ''}${key === today ? ' today' : ''}`;
    cell.title = `${key}${days.has(key) ? ' · practiced' : ''}`;
    element.append(cell);
  }
}
function renderProfile(fillForm = true) {
  const name = profile.name || 'MasCode User', handle = profile.handle || 'mascode-user';
  document.getElementById('sidebarProfileName').textContent = name;
  if (fillForm) {
    document.getElementById('profileName').value = profile.name || '';
    document.getElementById('profileHandle').value = profile.handle || '';
    document.getElementById('profileEmail').value = profile.email || '';
    document.getElementById('profileBio').value = profile.bio || '';
  }
  document.getElementById('profileDisplayName').textContent = name;
  document.getElementById('profileHandlePreview').textContent = `@${handle}`;
  document.getElementById('profileAvatar').textContent = name.trim().slice(0,1).toUpperCase() || 'M';
  const {current,longest,activeDays}=streakStats();
  document.getElementById('profileStreakStats').innerHTML = `<div class="profile-stat"><b>${current}</b><span>Current streak</span></div><div class="profile-stat"><b>${longest}</b><span>Longest streak</span></div><div class="profile-stat"><b>${activeDays}</b><span>Active days</span></div>`;
  renderHeatmap(document.getElementById('profileHeatmap'));
}
function renderProgress() {
  const solved = new Set(progress.solved), {current,longest,activeDays}=streakStats();
  document.getElementById('progressStats').innerHTML = `<div class="profile-stat"><b>${solved.size}<small> / 150</small></b><span>Problems solved</span></div><div class="profile-stat"><b>${current}</b><span>Current streak</span></div><div class="profile-stat"><b>${longest}</b><span>Longest streak</span></div><div class="profile-stat"><b>${activeDays}</b><span>Practice days</span></div>`;
  renderHeatmap(document.getElementById('progressHeatmap'));
  const topics = new Map();
  for (const p of problems) { const entry=topics.get(p.topic)||{total:0,solved:0}; entry.total++; if (solved.has(p.id)) entry.solved++; topics.set(p.topic,entry); }
  const list=document.getElementById('topicProgress'); list.replaceChildren();
  for (const [topic,count] of topics) {
    const row=document.createElement('div'); row.className='topic-row';
    const title=document.createElement('div'); title.className='topic-row-title';
    const label=document.createElement('b'); label.textContent=topic;
    const value=document.createElement('span'); value.textContent=`${count.solved} / ${count.total}`;
    title.append(label,value);
    const track=document.createElement('div'); track.className='progress-track';
    const fill=document.createElement('i'); fill.style.width=`${count.total ? count.solved/count.total*100 : 0}%`; track.append(fill);
    row.append(title,track); list.append(row);
  }
  document.getElementById('topicSolvedLabel').textContent=`${solved.size} of 150`;
  renderProfile(false);
}
function markProblemSolved(problem) {
  if (!progress.solved.includes(problem.id)) progress.solved.push(problem.id);
  const today=dateKey(); if (!progress.days.includes(today)) progress.days.push(today);
  storageWrite('mascode-progress-v1',progress); renderProgress();
}
function advanceToNextUnsolved(problem) {
  const index=problems.findIndex(item=>item.id===problem.id);
  const ordered=[...problems.slice(index+1),...problems.slice(0,index+1)];
  const next=ordered.find(item=>!progress.solved.includes(item.id));
  if (!next) {
    status.textContent='COMPLETE';
    setEvaluation('accepted','NeetCode 150 complete','You have solved all 150 problems.');
    return;
  }
  search.value=''; renderProblemOptions();
  selector.value=next.id;
  loadProblem(next.id);
}
function openPanel(view) {
  const overlay=document.getElementById('panelOverlay'); overlay.hidden=false;
  document.getElementById('progressView').hidden=view!=='progress';
  document.getElementById('profileView').hidden=view!=='profile';
  document.getElementById('panelTitle').textContent=view==='progress'?'Progress':'Profile';
  document.querySelectorAll('.sidebar .nav').forEach(button=>button.classList.toggle('active',button.id===(view==='progress'?'progressNav':'profileNav')));
  renderProgress();
  if(view==='profile')renderProfile(true);
}
function closePanel() {
  document.getElementById('panelOverlay').hidden=true;
  document.querySelectorAll('.sidebar .nav').forEach(button=>button.classList.toggle('active',button.id==='workspaceNav'));
}
function resetProgress(which) {
  const copy={solved:[...progress.solved],days:[...progress.days]};
  if (which==='solved') progress.solved=[];
  else if (which==='streak') progress.days=[];
  else progress={solved:[],days:[]};
  const label=which==='solved'?'solved problem progress':which==='streak'?'streak history':'all progress';
  if (!window.confirm(`Reset ${label}? This cannot be undone.`)) { progress=copy; return; }
  storageWrite('mascode-progress-v1',progress); renderProgress();
}

language.addEventListener('change', () => { saveDraft(); setStarter(); updateTestAvailability(); });
editor.setValue(''); updateTestAvailability();
editor.on('change', () => {
  clearDiagnostics(); saveDraft();
  clearTimeout(syntaxCheckTimer);
  const requestId = ++syntaxRequestId, source = editor.getValue(), lang = language.value;
  if (!source.trim()) return;
  syntaxCheckTimer = setTimeout(async () => {
    try {
      const result = await window.mascode.checkSyntax({ language: lang, code: source });
      if (requestId !== syntaxRequestId || language.value !== lang || editor.getValue() !== source) return;
      showDiagnostics(diagnosticsFrom(result.stderr, lang));
    } catch (_) { /* Syntax checking is optional when a local compiler is unavailable. */ }
  }, 650);
});

function renderProblemOptions(filter = '') {
  const query = filter.trim().toLowerCase();
  const visible = problems.filter(p => `${p.title} ${p.topic} ${p.difficulty}`.toLowerCase().includes(query));
  const selected = selector.value;
  selector.replaceChildren();
  const grouped = new Map();
  for (const item of visible) {
    if (!grouped.has(item.topic)) grouped.set(item.topic, []);
    grouped.get(item.topic).push(item);
  }
  for (const [topic, items] of grouped) {
    const group = document.createElement('optgroup'); group.label = topic;
    for (const item of items) {
      const option = document.createElement('option'); option.value = item.id;
      option.textContent = `${item.title} · ${item.difficulty}`; group.append(option);
    }
    selector.append(group);
  }
  if (!visible.length) {
    const option = document.createElement('option'); option.textContent = 'No matching problems'; option.value = ''; selector.append(option);
  } else if (visible.some(p => p.id === selected)) selector.value = selected;
  else { selector.value = visible[0].id; loadProblem(visible[0].id); }
}

async function loadProblem(id) {
  saveDraft();
  saveComplexity();
  currentProblem = problems.find(p => p.id === id) || null;
  const complexity=complexityByProblem[currentProblem?.id]||{};
  document.getElementById('timeComplexity').value=complexity.time||'';
  document.getElementById('spaceComplexity').value=complexity.space||'';
  document.getElementById('problemTitle').textContent = currentProblem?.title || 'Choose a problem';
  document.getElementById('questionDifficulty').textContent = currentProblem ? currentProblem.difficulty.toUpperCase() : 'SELECT A PROBLEM';
  document.getElementById('questionInfo').textContent = currentProblem
    ? `${currentProblem.topic} · ${currentProblem.testCount} bundled test functions. Python function signature is loaded into the editor.`
    : 'Choose a problem to load its function signature and test cases.';
  renderQuestion(currentProblem);
  document.getElementById('showAnswer').disabled = !currentProblem;
  document.getElementById('showTests').disabled = !currentProblem;
  answerVisible = false; testsVisible = false;
  document.getElementById('showAnswer').textContent = 'Show answer';
  document.getElementById('showTests').textContent = currentProblem ? `Show bundled tests (${currentProblem.testCount} functions)` : 'Show bundled test suite';
  const solutionCode = document.getElementById('solutionCode');
  solutionCode.hidden = true; solutionCode.textContent = 'Select a problem, then reveal its answer.';
  const testcaseCode = document.getElementById('testcaseCode');
  testcaseCode.hidden = true; testcaseCode.textContent = '';
  setStarter(); updateTestAvailability();
  if (currentProblem) {
    try { testcaseCode.textContent = await window.mascode.readTests(currentProblem.id); }
    catch (error) { testcaseCode.textContent = `Could not load bundled cases: ${error.message}`; }
  }
}

search.addEventListener('input', () => renderProblemOptions(search.value));
selector.addEventListener('change', () => loadProblem(selector.value));
document.getElementById('showTests').addEventListener('click', e => {
  testsVisible = !testsVisible;
  document.getElementById('testcaseCode').hidden = !testsVisible;
  e.currentTarget.textContent = testsVisible ? 'Hide test suite' : `Show bundled tests (${currentProblem.testCount} functions)`;
});
document.getElementById('showAnswer').addEventListener('click', async e => {
  if (!currentProblem) return;
  const code = document.getElementById('solutionCode');
  if (!answerVisible) {
    code.textContent = await window.mascode.readSolution(currentProblem.id);
    code.hidden = false; answerVisible = true; e.currentTarget.textContent = 'Hide answer';
  } else { code.hidden = true; answerVisible = false; e.currentTarget.textContent = 'Show answer'; }
});

const runCode = async () => {
  status.textContent = 'RUNNING';
  setEvaluation('idle','Running locally','Compiling and running your program on this device.');
  document.getElementById('caseResults').replaceChildren();
  document.getElementById('evalMetrics').hidden=true;
  document.querySelectorAll('.run-btn').forEach(b => b.disabled = true);
  try {
    const result = await window.mascode.compileRun({language: language.value, code: editor.getValue(), input: document.getElementById('stdin').value});
    const success=result.code===0, compileError=result.phase==='compile';
    setEvaluation(success?'accepted':compileError?'compile-error':'runtime-error',success?'Program finished':compileError?'Compilation error':result.timedOut?'Time limit exceeded':'Runtime error',success?'Your program ran successfully.':result.timedOut?'The program exceeded the local time limit.':'Review the error details below.');
    document.getElementById('consoleLabel').textContent=result.stderr?'ERROR DETAILS':'PROGRAM OUTPUT';
    document.getElementById('consoleOutput').textContent=[result.stdout,result.stderr].filter(Boolean).join('\n')||'(No output)';
    showDiagnostics(diagnosticsFrom(result.stderr, language.value));
    status.textContent = success ? 'DONE' : 'ERROR';
  } catch (e) { setEvaluation('runtime-error','Could not run program',e.message); status.textContent = 'ERROR'; }
  finally { document.querySelectorAll('.run-btn').forEach(b => b.disabled = false); }
};
function setEvaluation(kind,title,detail) {
  const summary=document.getElementById('resultSummary');
  summary.className=`result-summary result-${kind}`;
  summary.replaceChildren();
  const heading=document.createElement('b'); heading.textContent=title;
  const description=document.createElement('span'); description.textContent=detail;
  summary.append(heading,description);
}
function addMetric(label,value,kind='') {
  const box=document.createElement('div'); box.className=`eval-metric ${kind}`;
  const number=document.createElement('b'); number.textContent=value;
  const caption=document.createElement('span'); caption.textContent=label;
  box.append(number,caption); document.getElementById('evalMetrics').append(box);
}
function formatRuntime(milliseconds = 0) {
  const ms=Number(milliseconds)||0;
  return ms<1000?`${ms.toFixed(2)} ms`:`${(ms/1000).toFixed(2)} s`;
}
function showCaseCard(name,passed,detail='') {
  const card=document.createElement('article'); card.className=`case-card ${passed?'case-pass':'case-fail'}`;
  const top=document.createElement('div'); top.className='case-card-top';
  const title=document.createElement('b'); title.textContent=name.replace(/^test_/,'').replaceAll('_',' ');
  const badge=document.createElement('span'); badge.textContent=passed?'PASSED':'FAILED';
  top.append(title,badge); card.append(top);
  if (detail) { const message=document.createElement('p'); message.textContent=detail; card.append(message); }
  document.getElementById('caseResults').append(card);
}
const runTests = async (submission = false) => {
  if (!currentProblem || language.value !== 'python') return;
  const submittedProblem=currentProblem, submittedCode=editor.getValue();
  const submittedTimeComplexity=document.getElementById('timeComplexity').value.trim()||'—';
  const submittedSpaceComplexity=document.getElementById('spaceComplexity').value.trim()||'—';
  saveDraft(); status.textContent = 'TESTING';
  saveComplexity();
  setEvaluation('idle',submission?'Submitting solution':'Running test cases',`Evaluating ${submittedProblem.testCount} bundled test functions locally.`);
  document.getElementById('caseResults').replaceChildren();
  const metrics=document.getElementById('evalMetrics'); metrics.replaceChildren(); metrics.hidden=false;
  document.getElementById('consoleLabel').textContent='TEST RUN DETAILS';
  document.getElementById('consoleOutput').textContent='';
  document.getElementById('runTestsBtn').disabled = true;
  document.getElementById('submitBtn').disabled = true;
  try {
    const result = await window.mascode.runTests({id: submittedProblem.id, code: submittedCode});
    const summary = result.stdout.match(/RESULT\|(\d+)\|(\d+)\|(\d+)/);
    const passedCount=summary?Number(summary[1]):0, failedCount=summary?Number(summary[2]):(result.code===0?0:1), totalCount=summary?Number(summary[3]):submittedProblem.testCount;
    const accepted=result.code===0 && failedCount===0;
    setEvaluation(accepted?'accepted':'wrong-answer',accepted?(submission?'Accepted':'All tests passed'):'Not accepted',accepted?`All bundled tests passed in ${formatRuntime(result.elapsedMs)}.`:`${failedCount} test function${failedCount===1?'':'s'} need attention.`);
    addMetric('Passed',passedCount,'metric-pass'); addMetric('Failed',failedCount,'metric-fail'); addMetric('Total',totalCount);
    addMetric('Runtime',formatRuntime(result.elapsedMs),'metric-runtime');
    addMetric('Time complexity',submittedTimeComplexity,'metric-complexity');
    addMetric('Space complexity',submittedSpaceComplexity,'metric-complexity');
    for (const line of result.stdout.split('\n')) {
      const pass=line.match(/^PASS\|(.+)$/); if (pass) showCaseCard(pass[1],true);
      const fail=line.match(/^FAIL\|([^|]+)\|(.*)$/); if (fail) showCaseCard(fail[1],false,fail[2]);
    }
    if (!result.stdout.match(/^(PASS|FAIL)\|/m)) showCaseCard('Test runner',false,result.stderr||result.stdout||'Tests could not start.');
    document.getElementById('consoleOutput').textContent=result.stderr|| (accepted?'All test functions completed successfully.':'See failed test cards above for details.');
    showDiagnostics(diagnosticsFrom(`${result.stdout}\n${result.stderr}`, 'python'));
    status.textContent = accepted ? (submission?'ACCEPTED':'PASSED') : 'FAILED';
    if (accepted && submission) {
      markProblemSolved(submittedProblem);
      status.textContent='ACCEPTED';
      setEvaluation('accepted','Accepted · moving to next problem',`All tests passed in ${formatRuntime(result.elapsedMs)}. Your progress was saved.`);
      setTimeout(()=>advanceToNextUnsolved(submittedProblem),700);
    }
  } catch (error) { setEvaluation('runtime-error','Test runner error',error.message); document.getElementById('consoleOutput').textContent=error.message; status.textContent = 'ERROR'; }
  finally { updateTestAvailability(); }
};
document.getElementById('runBtn').addEventListener('click', runCode);
document.getElementById('runTop').addEventListener('click', runCode);
document.getElementById('runTestsBtn').addEventListener('click', runTests);
document.getElementById('submitBtn').addEventListener('click', () => runTests(true));
document.getElementById('timeComplexity').addEventListener('input',saveComplexity);
document.getElementById('spaceComplexity').addEventListener('input',saveComplexity);
document.addEventListener('keydown', e => { if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') { e.preventDefault(); language.value === 'python' ? runTests() : runCode(); } });
document.getElementById('progressNav').addEventListener('click', () => openPanel('progress'));
document.getElementById('profileNav').addEventListener('click', () => openPanel('profile'));
document.getElementById('closePanel').addEventListener('click', closePanel);
document.getElementById('workspaceNav').addEventListener('click', closePanel);
document.getElementById('panelOverlay').addEventListener('click', e => { if (e.target.id==='panelOverlay') closePanel(); });
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!document.getElementById('panelOverlay').hidden)closePanel();});
document.getElementById('resetSolved').addEventListener('click', () => resetProgress('solved'));
document.getElementById('resetStreak').addEventListener('click', () => resetProgress('streak'));
document.getElementById('resetAll').addEventListener('click', () => resetProgress('all'));
document.getElementById('profileForm').addEventListener('submit', e => {
  e.preventDefault();
  profile={name:document.getElementById('profileName').value.trim()||'MasCode User',handle:document.getElementById('profileHandle').value.trim().replace(/^@/,'')||'mascode-user',email:document.getElementById('profileEmail').value.trim(),bio:document.getElementById('profileBio').value.trim()};
  storageWrite('mascode-profile-v1',profile); renderProfile();
  const note=document.getElementById('profileSaved'); note.textContent='Profile saved on this device';
});
renderProfile();
document.getElementById('officialLink').addEventListener('click', () => window.mascode.openExternal(currentProblem?.problemUrl || 'https://neetcode.io/practice/practice/neetcode150'));
document.getElementById('roadmapNav').addEventListener('click', () => window.mascode.openExternal('https://neetcode.io/practice/practice/neetcode150'));
window.mascode.solutionsList().then(items => {
  problems = items; renderProblemOptions();
  renderProgress();
  document.getElementById('questionInfo').textContent = 'All 150 Python function starters, reference answers, and bundled test suites are available offline.';
}).catch(error => { selector.replaceChildren(new Option('Could not load problem list', '')); document.getElementById('questionInfo').textContent = error.message; });
window.mascode.systemInfo().then(info => {
  document.getElementById('cpuLabel').textContent = `${info.cpu} · ${info.cores} cores`;
  document.getElementById('systemLine').textContent = `${info.platform} · ${info.cores} logical cores · ${(info.memory/1024**3).toFixed(1)} GB RAM`;
});
