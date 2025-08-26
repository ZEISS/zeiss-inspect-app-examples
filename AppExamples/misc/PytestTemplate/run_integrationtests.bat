@echo off
:: ###########################################################################
:: run_integrationtests.bat
::
:: Run ZEISS INSPECT integration tests from Windows command line
::
:: NOTE: There also is a PowerShell script as the preferred alternative!
::
:: * Requires ZEISS INSPECT >= 2025.
:: * Set ZIX_VERSIONS to the ZEISS INSPECT versions you want to use for testing
:: * The App must be set up in the ZEISS INSPECT App explorer; either
::   installed and in editing mode or in a connected folder.
:: * If the script path scripts/tests/run_integrationtests.py referred to
::   by TESTRUNNER (see below) is not unique within all installed/connected
::   Apps, specify it with the App's UUID as parameter.
:: * See scripts/tests/log/ for logfiles.
:: * See doc/ for more information.
:: ###########################################################################

setlocal

set ZIX_VERSIONS=2025 2026

:: Use the second variant (with the App's UUID) if the script's pathname is ambiguous
set TESTRUNNER="gom.script.userscript.tests__run_integrationtests()"
:: set TESTRUNNER="gom.script.userscript.tests__run_integrationtests('d085fe43-f802-4e28-8620-1751fc300a66')"

for %%V in (%ZIX_VERSIONS%) do (
    echo Testing in ZEISS INSPECT %%V
    set "ZEISS_INSPECT_EXE=C:\Program Files\Zeiss\INSPECT\%%V\bin\ZEISS_INSPECT.exe"
    
    call "%%ZEISS_INSPECT_EXE%%" -eval %%TESTRUNNER%% -minimized -nosplash
)

:: Create and activate a virtual Python environment
for /f "tokens=1" %%i in ("%ZIX_VERSIONS%") do set VERSION=%%i
set "PYTHON_EXE=C:\Program Files\Zeiss\INSPECT\%VERSION%\python\python.exe"

call "%PYTHON_EXE%" -m venv venv
call .\venv\scripts\activate.bat

:: Install coverage in the virtual environment
call pip install coverage

:: Copy Pytest coverage data
copy .coverage .coverage.pytest

:: Combine the coverage data from pytest and from all services
coverage combine --data-file=.\.coverage --keep scripts\services\ .coverage.pytest

:: Create HTML report of combined coverage results
coverage html --data-file=.\.coverage --omit=*/Local/Temp/* -d scripts\tests\reports\cov\html_combined

:: Create HTML report of combined coverage results
coverage xml --data-file=.\.coverage --omit=*/Local/Temp/* -o scripts\tests\reports\cov\integrationtest-combined-coverage.xml

:: Deactivate virtual environment
call .\venv\scripts\deactivate.bat 

endlocal
