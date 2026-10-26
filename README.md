# MasCode

MasCode is a desktop coding practice app that runs code on your own computer. It includes a syntax-highlighted editor, local compiler/runtime integration for C++, Python, and Java, and an offline practice set based on the NeetCode 150 roadmap.

## Features

- Edit code with syntax highlighting, indentation, and syntax checks.
- Compile and run C++ and Java, and run Python using locally installed language tools.
- Browse 150 practice problems with descriptions, examples, constraints, Python starter functions, reference solutions, and bundled tests.
- Track solved problems, activity streaks, and profile details locally.
- See test results, measured runtime, and submitted time/space complexity estimates.

The bundled problem runner currently evaluates Python solutions. The editor's C++, Python, and Java run controls execute user code locally; C++ and Java are not wired into the bundled problem test suites.

## Install a packaged release

Download the release for your operating system from [GitHub Releases](https://github.com/Santhoshkkumart/mascode/releases). If no release is available yet, build from source using the instructions below.

### Windows

1. Download `MasCode-<version>-Setup.exe` and run it.
2. Install the language tools you need and make sure they are available on `PATH`:
   - C++: `g++` (for example, through [MSYS2](https://www.msys2.org/), using the UCRT64 environment)
   - Python: Python 3, available as `python`
   - Java: a JDK, providing `java` and `javac`

The Windows installer is currently unsigned, so Windows may display a publisher warning.

### Linux

1. Download `MasCode-<version>-x86_64.AppImage`.
2. In a terminal, make it executable and launch it:

   ```sh
   chmod +x MasCode-<version>-x86_64.AppImage
   ./MasCode-<version>-x86_64.AppImage
   ```

If the AppImage cannot start because FUSE is unavailable, try:

```sh
./MasCode-<version>-x86_64.AppImage --appimage-extract-and-run
```

Install the language tools you plan to use through your distribution's package manager. They must be available on `PATH` (`g++`, Python 3, and/or a JDK). MasCode currently publishes an AppImage rather than a DEB or RPM package.

## Build from source

### Requirements

- Git
- Node.js 22 or newer and npm
- A C++ compiler, Python 3, and/or a JDK for the languages you plan to run

Clone the repository, install dependencies, and start the development app:

```sh
git clone https://github.com/Santhoshkkumart/mascode.git
cd mascode
npm ci
npm start
```

Build a distributable on the corresponding operating system:

```sh
# Linux: AppImage
npm run dist:linux

# Windows: NSIS installer and ZIP archive (run on Windows)
npm run dist:windows
```

Build artifacts are written to `release/`. Windows packages are built on Windows; Linux AppImages are built on Linux.

## Automated builds and releases

GitHub Actions builds Linux and Windows packages for pushes, pull requests, and manual workflow runs. Download those build artifacts from the corresponding workflow run.

To publish a GitHub Release, update the version in `package.json`, commit and push the change, then create and push a version tag. For example:

```sh
git tag v1.0.1
git push origin v1.0.1
```

The tag workflow builds both platforms and attaches the installers to a GitHub Release. GitHub Actions requires the repository's default `GITHUB_TOKEN` to have permission to create releases; the workflow grants `contents: write` to its release job.

## Progress and local data

Problem progress, activity streaks, and profile details are stored on the device in the app's local storage. They are not synchronized between computers.

## Attribution and licenses

The bundled problem descriptions, examples, constraints, Python reference solutions, and tests are based on [richard7ao/neetcode-150](https://github.com/richard7ao/neetcode-150), commit `83adb3ffd8e674ea00d7d763a77c130d57ff8cb9`, under the Apache License 2.0. The license is included at `src/solutions/LICENSE`. That project attributes solution code to [jomalonelondon/neetcode-solutions](https://github.com/jomalonelondon/neetcode-solutions), also under Apache 2.0. MasCode's bundled tests are local practice tests; they do not include hidden platform tests. See the [official NeetCode 150 roadmap](https://neetcode.io/practice/practice/neetcode150).

## Running code safely

Programs run with the current operating-system user's permissions. The runner is intended for code you trust, not untrusted programs. C++ and Java compile in a temporary directory, Python runs directly, and temporary files are removed after execution.
