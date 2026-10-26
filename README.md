# MasCode

MasCode is a local-first coding practice desktop app. Its embedded editor highlights C++, Python, and Java, checks syntax as you type, and runs programs using the compilers installed on your computer. Code is not sent to a cloud compiler.

## Install a release

Download the installer for your operating system from the repository's **GitHub Releases** page.

### Windows

1. Download `MasCode-<version>-Setup.exe`.
2. Run it and follow the installer. It installs for your Windows user and adds a Start menu shortcut; the desktop shortcut can be selected in setup.
3. Install the language tools you want to use and add them to `PATH`:
   - C++: `g++` (for example, MSYS2 MinGW UCRT64)
   - Python: Python 3 (`python` command)
   - Java: JDK (`java` and `javac` commands)

### Linux

Choose one of the release formats:

- **AppImage** works on most desktop Linux distributions without installation. Make it executable and launch it:

  ```sh
  chmod +x MasCode-<version>-x86_64.AppImage
  ./MasCode-<version>-x86_64.AppImage
  ```

If the AppImage cannot mount because FUSE support is missing, launch it with `./MasCode-<version>-x86_64.AppImage --appimage-extract-and-run`.

Ubuntu/Debian users can run the AppImage above; the release does not currently include a DEB installer.

Install the language tools you need (`g++`, Python 3, and/or a JDK) using your distribution's package manager. They must be available on `PATH`.

## Build from source

Requirements: Node.js 22 or newer, npm, and Git. Install the compilers/runtimes for the languages you plan to use as described above.

```sh
git clone <your-github-repository-url>
cd mascode
npm ci
npm start
```

Build installers on their target operating system:

```sh
# Linux: AppImage
npm run dist:linux

# Windows: NSIS installer and ZIP archive (run this on Windows)
npm run dist:windows
```

Build outputs go to `release/`. The Linux and Windows GitHub Actions workflow builds both sets of installers when code is pushed. Push a version tag such as `v1.0.1` to create a GitHub Release with the installers attached. The build does not sign the Windows installer; Windows may show the standard publisher warning for unsigned apps.

After creating an empty GitHub repository, connect and push this folder:

```sh
git remote add origin https://github.com/<your-name>/<repo-name>.git
git push -u origin main
```

For a release, make sure `package.json` has the version you want (for example `1.0.0`), commit and push that change, then tag it with the `v` prefix:

```sh
git tag v1.0.0
git push origin v1.0.0
```

## Practice and progress

The NeetCode 150 selector includes 150 problem descriptions, examples, constraints, Python function starters, reference answers, and test suites offline. Select a problem to load its blank function into the editor. **Run test cases** checks it without marking the problem solved; **Submit solution** checks all bundled tests, records accepted progress, and advances to the next unsolved problem. You can enter Big O time and space estimates to include in the result; MasCode measures runtime but does not infer asymptotic complexity.

The Progress menu tracks solved problems by topic and daily activity streaks. Profile details and progress are stored locally on the device.

## Attribution and licenses

The bundled Python solutions, problem descriptions, examples, constraints, and test suites are from [richard7ao/neetcode-150](https://github.com/richard7ao/neetcode-150), commit `83adb3ffd8e674ea00d7d763a77c130d57ff8cb9`, under Apache License 2.0. The license is included at `src/solutions/LICENSE`. That project attributes solution code to [jomalonelondon/neetcode-solutions](https://github.com/jomalonelondon/neetcode-solutions), also Apache 2.0. Hidden platform tests are not included; visit the [official NeetCode page](https://neetcode.io/practice/practice/neetcode150) for the official roadmap.

## Local execution note

Programs run with your operating-system user permissions. The runner is intended for your own code, not untrusted programs. C++ and Java compile in a temporary directory; Python runs directly. Temporary source and binaries are removed after each run.
