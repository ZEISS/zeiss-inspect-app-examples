###############################################################################
# run_tests.ps1 - Run ZEISS INSPECT integration tests from Windows command line
#
#
# * Requires ZEISS INSPECT >= 2025.
# * Set zixVersions to the ZEISS INSPECT versions you want to use for testing.
# * The App must be set up in the ZEISS INSPECT App explorer; either
#   installed and in editing mode or in a connected folder.
# * If the script path scripts/tests/testrunner.py referred to by testRunner
#   (see below) is not unique within all installed/connected Apps,
#   specify it with the App's UUID as parameter.
# * See scripts/tests/log/ for logfiles.
# * See doc/ for more information.
###############################################################################

$zixVersions = @(2025, 2026)

# Use the second variant (with the App's UUID) if the script's pathname is ambiguous
$testRunner = "gom.script.userscript.tests__testrunner()"
#$testRunner = "gom.script.userscript.tests__testrunner('d085fe43-f802-4e28-8620-1751fc300a66')"

foreach ($version in $zixVersions) {
    $inspectExe = "C:/Program Files/Zeiss/INSPECT/$version/bin/ZEISS_INSPECT.exe"

    Write-Host "Testing with ZEISS INSPECT version $version"
    Start-Process -FilePath $inspectExe -ArgumentList "-eval", "$testRunner", "-minimized", "-nosplash" -Wait
}
