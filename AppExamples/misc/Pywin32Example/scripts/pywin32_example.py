# -*- coding: utf-8 -*-
#
# pywin32_example.py
#
# Demonstrates how to use pywin32 in a ZEISS INSPECT App.
#
# Carl Zeiss GOM Metrology GmbH, 2026
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2027/python_examples/examples_overview.html
# ---

# Note: Prior to ZEISS INSPECT 2027, pywin32 could not be imported directly after
# wheel installation, because ZEISS INSPECT did not process .pth files in its wheel cache.
# A helper module setup_pywin32 replicates the necessary initialization.

import gom
import win32api
import win32con
import pywintypes


def get_windows_info():
    """Retrieve basic Windows system information using pywin32."""

    # -------------------------------------------------------------------------
    # Get Windows version
    # -------------------------------------------------------------------------
    version_info = win32api.GetVersionEx()
    major = version_info[0]
    minor = version_info[1]
    build = version_info[2]
    windows_version = f"{major}.{minor} (Build {build})"

    # -------------------------------------------------------------------------
    # Get computer name and user name
    # -------------------------------------------------------------------------
    computer_name = win32api.GetComputerName()
    user_name = win32api.GetUserName()

    # -------------------------------------------------------------------------
    # Get system directory
    # -------------------------------------------------------------------------
    system_dir = win32api.GetSystemDirectory()

    return {
        'windows_version': windows_version,
        'computer_name': computer_name,
        'user_name': user_name,
        'system_dir': system_dir,
    }


def read_registry_value(key_path, value_name):
    """
    Read a string value from HKEY_LOCAL_MACHINE registry.

    Parameters:
        key_path  - registry key path, e.g. r'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion'
        value_name - value name, e.g. 'ProductName'

    Returns:
        The registry value as a string, or None if not found.
    """
    # -------------------------------------------------------------------------
    # Open the registry key and read the value
    # -------------------------------------------------------------------------
    try:
        key = win32api.RegOpenKey(
            win32con.HKEY_LOCAL_MACHINE,
            key_path,
            0,
            win32con.KEY_READ | win32con.KEY_WOW64_64KEY
        )
        value, _ = win32api.RegQueryValueEx(key, value_name)
        win32api.RegCloseKey(key)
        return value
    except pywintypes.error:
        return None


if __name__ == '__main__':
    # -------------------------------------------------------------------------
    # Print Windows system information
    # -------------------------------------------------------------------------
    info = get_windows_info()
    print("=== Windows System Information (via pywin32) ===")
    print(f"  Windows version : {info['windows_version']}")
    print(f"  Computer name   : {info['computer_name']}")
    print(f"  User name       : {info['user_name']}")
    print(f"  System directory: {info['system_dir']}")

    # -------------------------------------------------------------------------
    # Read Windows product name from registry
    # -------------------------------------------------------------------------
    product_name = read_registry_value(
        r'SOFTWARE\Microsoft\Windows NT\CurrentVersion',
        'ProductName'
    )
    if product_name:
        print(f"  Windows product : {product_name}")

    print("\npywin32 is working correctly in this ZEISS INSPECT App.")
