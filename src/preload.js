const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('mascode', {
  systemInfo: () => ipcRenderer.invoke('system-info'),
  solutionsList: () => ipcRenderer.invoke('solutions-list'),
  readSolution: (id) => ipcRenderer.invoke('solution-read', id),
  readTests: (id) => ipcRenderer.invoke('tests-read', id),
  runTests: (payload) => ipcRenderer.invoke('run-problem-tests', payload),
  checkSyntax: (payload) => ipcRenderer.invoke('check-syntax', payload),
  compileRun: (payload) => ipcRenderer.invoke('compile-run', payload),
  openExternal: (url) => ipcRenderer.invoke('open-external', url)
});
