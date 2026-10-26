# MasCode

MasCode is a local-first Electron coding workspace. Its embedded editor highlights C++, Python, and Java syntax, checks for compile/syntax errors while you type, underlines the affected line, and auto-indents when you press Enter. Tab inserts four spaces. Programs run with tools installed on your computer.

## Run

1. Install Node.js and npm.
2. Install the compilers/runtimes you want and make them available on `PATH`: `g++`, `python3` (Windows: `python`), and `javac`/`java`.
3. Run `npm install`, then `npm start`.

The NeetCode 150 selector includes all 150 full problem descriptions, examples, constraints, Python function starters, reference solutions, and bundled test suites offline. Select a problem to see its whole question and examples, load its empty function signature into the editor, reveal the complete test file, then use **Run test cases** to execute every included case. The reference answer stays separate from the editor. The test harness runs Python 3; C++17 and Java remain available in the standalone local runner.

The **Progress** menu tracks solved problems by topic and records activity streaks. The **Profile** menu lets you edit a display name, username, email, and bio; these and progress are stored locally in the app. **Submit solution** evaluates every bundled test, shows boxed pass/fail results and elapsed runtime, and updates progress when accepted. You can enter your own Big O time and space estimates; MasCode does not try to infer asymptotic complexity from code.

## Answer attribution

The bundled Python solutions, problem descriptions, examples, constraints, and test suites are from [richard7ao/neetcode-150](https://github.com/richard7ao/neetcode-150), commit `83adb3ffd8e674ea00d7d763a77c130d57ff8cb9`, and are distributed under Apache License 2.0. The required license is included at `src/solutions/LICENSE`. The upstream project attributes its solution code to [jomalonelondon/neetcode-solutions](https://github.com/jomalonelondon/neetcode-solutions), also Apache 2.0. Hidden platform tests aren’t bundled; use the [official NeetCode page](https://neetcode.io/practice/practice/neetcode150) for those.

## Local runner

Programs execute as your operating-system user. This runner is intended for your own code, not untrusted programs. C++ and Java compile in a temporary directory; Python runs directly. Temporary source and binaries are removed after each run.
