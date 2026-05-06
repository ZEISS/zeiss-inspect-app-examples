# -*- coding: utf-8 -*-
#
# setup_pywin32.py
#
# Carl Zeiss GOM Metrology GmbH, 2026
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2026/python_examples/examples_overview.html
# ---
#
# Helper module: manually set up pywin32 DLL path and sys.path entries.
#
# Background: ZEISS INSPECT uses a wheel cache to install Python packages, but
# does NOT process .pth files in that cache directory. Therefore, pywin32's
# pywin32.pth (which normally runs pywin32_bootstrap.py and calls
# os.add_dll_directory) is never executed, causing:
#
#   ModuleNotFoundError: No module named 'pywintypes'
#
# This module replicates what pywin32.pth + pywin32_bootstrap.py would do.
# Call setup_pywin32() before any pywin32-dependent import.

import glob
import os
import sys


def setup_pywin32():
    """
    Set up pywin32 DLL search path and sys.path entries manually.

    This is necessary because ZEISS INSPECT's wheel cache does not process
    .pth files, so pywin32.pth / pywin32_bootstrap.py are never executed.

    Must be called before any pywin32-dependent import (e.g. import win32api,
    import pywintypes, import fastmcp).
    """
    # -------------------------------------------------------------------------
    # Skip if already set up
    # -------------------------------------------------------------------------
    if 'pywintypes' in sys.modules:
        return

    import gom
    import gom.api.addons

    addon = gom.api.addons.get_current_addon()

    # -------------------------------------------------------------------------
    # Find the pywin32 wheel filename from the App's scripts/modules/ folder
    # -------------------------------------------------------------------------
    if addon.is_edited():
        # Edit mode: addon.get_file() returns the edit directory path
        addon_dir = addon.get_file()
        matches = glob.glob(
            os.path.join(addon_dir, 'scripts', 'modules', 'pywin32-*.whl')
        )
    else:
        # Installed (ZIP) mode: use get_file_list() and filter
        matches = [
            f for f in addon.get_file_list()
            if 'scripts/modules/pywin32-' in f.replace('\\', '/') and f.endswith('.whl')
        ]

    if not matches:
        raise RuntimeError(
            "pywin32 wheel not found in the App's scripts/modules/ folder. "
            "Please add the appropriate pywin32 wheel for your Python version "
            "(e.g. pywin32-311-cp313-cp313-win_amd64.whl)."
        )

    wheel_stem = os.path.splitext(os.path.basename(matches[0]))[0]

    # -------------------------------------------------------------------------
    # Locate the wheel cache directory
    # The glob handles any ZEISS INSPECT version (2027, 2028, ...)
    # -------------------------------------------------------------------------
    cache_dirs = glob.glob(
        os.path.join(
            os.environ['APPDATA'], 'gom', '*',
            'gom_python_wheel_cache', wheel_stem
        )
    )
    if not cache_dirs:
        raise RuntimeError(
            f"pywin32 wheel cache directory not found for wheel: {wheel_stem}\n"
            "Make sure the pywin32 wheel is installed in the App and the App "
            "has been started at least once so ZEISS INSPECT can populate the cache."
        )

    cache_dir = cache_dirs[0]

    # -------------------------------------------------------------------------
    # 1. Add the DLL directory so pywintypes<VER>.dll / pythoncom<VER>.dll
    #    can be found (replicates what pywin32_bootstrap.py does)
    #    e.g. pywintypes39.dll for Python 3.9, pywintypes313.dll for Python 3.13
    # -------------------------------------------------------------------------
    dll_dir = os.path.join(cache_dir, 'pywin32_system32')
    os.add_dll_directory(dll_dir)

    # -------------------------------------------------------------------------
    # 2. Add win32, win32\lib, Pythonwin to sys.path
    #    (replicates what pywin32.pth does)
    # -------------------------------------------------------------------------
    for sub in ('win32', os.path.join('win32', 'lib'), 'Pythonwin'):
        p = os.path.join(cache_dir, sub)
        if p not in sys.path:
            sys.path.insert(0, p)
