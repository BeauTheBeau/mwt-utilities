# MWT Utilities

A collection of utilities for MWT, an FPS-tycoon hybrid.

## Installation

[![Build Executable](https://github.com/BeauTheBeau/mwt-utilities/actions/workflows/build-executable.yml/badge.svg)](https://github.com/BeauTheBeau/mwt-utilities/actions/workflows/build-executable.yml)

### Prebuilt Binaries

MWT Utilities is available for x86_64 Windows and Linux. Binaries are automatically built and uploaded to the 
[releases page](https://github.com/BeauTheBeau/mwt-utilities/releases) on every commit to the `main` branch. Before 
installing, make sure you trust me and the code I write. I'm not responsible for any damage caused by this software.


### From Source

Alternatively, you can build the project yourself.

#### Prerequisites
- [Python 3.11](https://www.python.org/downloads/)
- [PyInstaller](https://www.pyinstaller.org/)

#### Building

1. Clone the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Run `pyinstaller --onefile --icon=icon.ico hold-to-lean/main.py` in the root directory of the repository
