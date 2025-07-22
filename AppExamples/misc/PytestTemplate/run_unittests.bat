@echo off
:: ###########################################################################
:: run_unittests.bat
::
:: Run ZEISS INSPECT App unit tests from Windows command line
::
:: NOTE: There also is a PowerShell script as the preferred alternative!
::
:: * Uses 
::   * pytest
::   * pytest-cov
::   * pytest-html
::   * pytest-xdist
::   -- install with initial run (see below)
:: * Set zixVersion to the ZEISS INSPECT version to select the Python interpreter
:: * Set ZIX_VERSIONS to the ZEISS INSPECT versions you want to use for testing
:: * See scripts/tests/log/ for logfiles.
:: * See doc/ for more information.
:: ###########################################################################

setlocal

set ZIX_VERSION=2025
set "PYTHON_EXE=C:\Program Files\Zeiss\INSPECT\%ZIX_VERSION%\python\python.exe"

:: Uncomment the following lines to install pytest and its
:: required submodules with initial run
rem call "%PYTHON_EXE%" -m pip install pytest
rem call "%PYTHON_EXE%" -m pip install pytest-cov
rem call "%PYTHON_EXE%" -m pip install pytest-html
rem call "%PYTHON_EXE%" -m pip install pytest-xdist

call "%PYTHON_EXE%" .\scripts\tests\run_unittests.py

endlocal
