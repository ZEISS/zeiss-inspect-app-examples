# Pywin32Example

Example demonstrating how to use the `pywin32` package in a ZEISS INSPECT App.

## Short description

This example shows how to use `pywin32` in ZEISS INSPECT 2027 or later.
A workaround for setting up `pywin32` in earlier versions of ZEISS INSPECT has been removed from this release.

## Requirements

- ZEISS INSPECT 2027 or later
- `pywin32` wheel matching the Python version used by ZEISS INSPECT, placed in `scripts/modules/`

## Installing the pywin32 wheel

Install `pywin32` into the App's `scripts/modules/` folder using the App Editor's **Install Python Packages** dialog (RMB on the `scripts` or `modules` folder ► Install Python Packages…). The App Editor automatically selects the wheel compatible with the Python version used by ZEISS INSPECT.

Alternatively, download the wheel for your Python version from [PyPI – pywin32 files](https://pypi.org/project/pywin32/#files) and add it via the **From local file system** option in the same dialog.

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
