@echo off
:: ###########################################################################
:: run_tests.bat
::
:: Run ZEISS INSPECT integration tests from Windows command line
::
:: NOTE: There also is a PowerShell script as the preferred alternative!
::
:: * Requires ZEISS INSPECT >= 2025.
:: * Set ZIX_VERSIONS to the ZEISS INSPECT versions you want to use for testing
:: * The App must be set up in the ZEISS INSPECT App explorer; either
::   installed and in editing mode or in a connected folder.
:: * If the script path scripts/tests/testrunner.py referred to by TESTRUNNER
::   (see below) is not unique within all installed/connected Apps,
::   specify it with the App's UUID as parameter.
:: * See scripts/tests/log/ for logfiles.
:: * See doc/ for more information.
:: ###########################################################################

setlocal

set ZIX_VERSIONS=2025 2026

:: Use the second variant (with the App's UUID) if the script's pathname is ambiguous
set TESTRUNNER="gom.script.userscript.tests__testrunner()"
:: set TESTRUNNER="gom.script.userscript.tests__testrunner('d085fe43-f802-4e28-8620-1751fc300a66')"

for %%V in (%ZIX_VERSIONS%) do (
    echo Testing in ZEISS INSPECT %%V
    set "ZEISS_INSPECT_EXE=C:\Program Files\Zeiss\INSPECT\%%V\bin\ZEISS_INSPECT.exe"
    
    call "%%ZEISS_INSPECT_EXE%%" -eval %%TESTRUNNER%% -minimized -nosplash
)

endlocal
