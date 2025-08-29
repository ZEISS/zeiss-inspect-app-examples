###############################################################################
# run_integrationtests.ps1
#
# Run ZEISS INSPECT integration tests from Windows PowerShell
#
# * Requires ZEISS INSPECT >= 2025.
# * Set zixVersions to the ZEISS INSPECT versions you want to use for testing.
# * The App must be set up in the ZEISS INSPECT App explorer; either
#   installed and in editing mode or in a connected folder.
# * If the script path scripts/tests/run_integrationtests.py referred to by
#   testRunner (see below) is not unique within all installed/connected Apps,
#   specify it with the App's UUID as parameter.
# * See scripts/tests/log/ for logfiles.
# * See doc/ for more information.
###############################################################################

$zixVersions = @(2025, 2026)

# Use the second variant (with the App's UUID) if the script's pathname is ambiguous
$testRunner = "gom.script.userscript.tests__run_integrationtests()"
#$testRunner = "gom.script.userscript.tests__run_integrationtests('d085fe43-f802-4e28-8620-1751fc300a66')"

foreach ($version in $zixVersions) {
    $inspectExe = "C:/Program Files/Zeiss/INSPECT/$version/bin/ZEISS_INSPECT.exe"

    Write-Host "Testing with ZEISS INSPECT version $version"
    Start-Process -FilePath $inspectExe -ArgumentList "-eval", "$testRunner", "-minimized", "-nosplash" -Wait
}

# Create and activate a virtual Python environment
$pythonExe = "C:\Program Files\Zeiss\INSPECT\$($zixVersions[0])\python\python.exe"
& $pythonExe -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install coverage in the virtual environment
pip install coverage

# Copy Pytest coverage data
copy .coverage .coverage.pytest

# Combine the coverage data from pytest and from all services
coverage combine --data-file=./.coverage --keep scripts/services/ scripts/scripted_elements/ .coverage.pytest

# Create HTML report of combined coverage results
coverage html --data-file=./.coverage --omit=*/Local/Temp/* -d scripts/tests/reports/cov/html_combined

# Create HTML report of combined coverage results
coverage xml --data-file=./.coverage --omit=*/Local/Temp/* -o scripts/tests/reports/cov/integrationtest-combined-coverage.xml

# Deactivate virtual environment
deactivate 