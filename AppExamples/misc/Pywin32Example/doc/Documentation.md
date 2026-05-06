# Pywin32Example

Example demonstrating how to use the `pywin32` package in a ZEISS INSPECT App.

## Short description

This example shows how to work around a known limitation of ZEISS INSPECT's wheel cache mechanism that prevents `pywin32` from being imported directly. It demonstrates retrieving Windows system information and reading registry values using `pywin32`.

## Requirements

- ZEISS INSPECT 2023 or later
- `pywin32` wheel matching the Python version used by ZEISS INSPECT, placed in `scripts/modules/`
  - Python 3.9 (ZEISS INSPECT 2023–2026): `pywin32-311-cp39-cp39-win_amd64.whl`
  - Python 3.13 (ZEISS INSPECT 2027+): `pywin32-311-cp313-cp313-win_amd64.whl`

## Background: Why pywin32 needs special handling

ZEISS INSPECT installs Python packages from a wheel cache at:
```
%APPDATA%\gom\<VERSION>\gom_python_wheel_cache\<WHEEL_STEM>\
```

However, Python's `.pth` file mechanism is **not processed** for this cache directory. Since `pywin32` relies on `pywin32.pth` to:
1. Add `win32\`, `win32\lib\`, `Pythonwin\` to `sys.path`
2. Run `pywin32_bootstrap.py`, which calls `os.add_dll_directory()` on `pywin32_system32\` (containing `pywintypes<VER>.dll`, `pythoncom<VER>.dll`, e.g. `pywintypes39.dll` for Python 3.9)

…a plain `import win32api` or `import pywintypes` fails with:

```
ModuleNotFoundError: No module named 'pywintypes'
```

## Workaround: `setup_pywin32.py`

The helper module `setup_pywin32.py` replicates what `pywin32.pth` and `pywin32_bootstrap.py` would normally do:

```python
from setup_pywin32 import setup_pywin32
setup_pywin32()

import win32api  # now works
```

`setup_pywin32()` does the following:

1. Uses `gom.api.addons` to find the `pywin32-*.whl` filename from the App's `scripts/modules/` folder (works in both edit mode and installed mode).
2. Locates the corresponding wheel cache directory.
3. Calls `os.add_dll_directory()` on `pywin32_system32\` so the DLLs can be found.
4. Adds `win32\`, `win32\lib\`, `Pythonwin\` to `sys.path`.

## Installing the pywin32 wheel

Install `pywin32` into the App's `scripts/modules/` folder using the App Editor's **Install Python Packages** dialog (RMB on the `scripts` or `modules` folder ► Install Python Packages…). The App Editor automatically selects the wheel compatible with the Python version used by ZEISS INSPECT.

Alternatively, download the wheel for your Python version from [PyPI – pywin32 files](https://pypi.org/project/pywin32/#files) and add it via the **From local file system** option in the same dialog.

| ZEISS INSPECT version | Python | Wheel filename |
|---|---|---|
| 2023–2026 | 3.9 | `pywin32-311-cp39-cp39-win_amd64.whl` |
| 2027+ | 3.13 | `pywin32-311-cp313-cp313-win_amd64.whl` |

When the App is started, ZEISS INSPECT automatically installs the wheel into its wheel cache.

## Example script: `pywin32_example.py`

Demonstrates two use cases:

### 1. Windows system information

```python
import win32api

version_info = win32api.GetVersionEx()
computer_name = win32api.GetComputerName()
user_name = win32api.GetUserName()
system_dir = win32api.GetSystemDirectory()
```

### 2. Registry access

```python
import win32api
import win32con
import pywintypes

key = win32api.RegOpenKey(
    win32con.HKEY_LOCAL_MACHINE,
    r'SOFTWARE\Microsoft\Windows NT\CurrentVersion',
    0,
    win32con.KEY_READ | win32con.KEY_WOW64_64KEY
)
value, _ = win32api.RegQueryValueEx(key, 'ProductName')
win32api.RegCloseKey(key)
```

## Expected output

```
=== Windows System Information (via pywin32) ===
  Windows version : 10.0 (Build 22631)
  Computer name   : MY-PC
  User name       : jdoe
  System directory: C:\Windows\system32
  Windows product : Windows 10 Pro

pywin32 is working correctly in this ZEISS INSPECT App.
```
