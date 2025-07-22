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
:: * See doc/ for more information.
:: ###########################################################################

setlocal

set ZIX_VERSION=2025
set "PYTHON_EXE=C:\Program Files\Zeiss\INSPECT\%ZIX_VERSION%\python\python.exe"

:: Comment out the following line to reduce startup time
call "%PYTHON_EXE%" -m pip install -r scripts\modules\requirements.txt

call "%PYTHON_EXE%" .\scripts\tests\run_unittests.py

endlocal
