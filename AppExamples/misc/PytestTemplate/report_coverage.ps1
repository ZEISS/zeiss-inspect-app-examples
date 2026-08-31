# Combine coverage data from pytest and ZEISS INSPECT services
#
# Requires ZEISS INSPECT >= 2027.
#
# Carl Zeiss GOM Metrology GmbH, 2026
# ------------------------------------------------------------------------------------------------

$appRoot = $PSScriptRoot
Set-Location -LiteralPath $appRoot

# Python executable path
$pythonExe = "$env:LOCALAPPDATA\Programs\Python\Python314\python.exe"
if (-not (Test-Path -LiteralPath $pythonExe -PathType Leaf)) {
	throw "Python executable was not found at $pythonExe. Update the path defined by `$pythonExe`."
}

# Create and activate a virtual Python environment
& $pythonExe -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install coverage in the virtual environment
pip install coverage

# Combine the coverage data from pytest and all services
if (Test-Path -LiteralPath "cov_temp" -PathType Container) {
	coverage combine --data-file=./.coverage --keep cov_temp
}

# Ignore ZEISS INSPECT virtual module paths that have no local source file.
# $coverageOmit = "*/Local/Temp/*,:*.scripts.*,*/gom.__*"
$coverageOmit = "*/Local/Temp/*,*/gom.__*"
$coverageDataFile = Join-Path $appRoot ".coverage"
$coverageReportDirectory = Join-Path $appRoot "scripts/tests/reports/cov/html_combined"
$coverageXmlFile = Join-Path $appRoot "scripts/tests/reports/cov/integrationtest-combined-coverage.xml"
New-Item -ItemType Directory -Path $coverageReportDirectory -Force | Out-Null

# Create HTML report of combined coverage results
coverage html --data-file=$coverageDataFile --omit=$coverageOmit --ignore-errors -d $coverageReportDirectory

# Create HTML report of combined coverage results
coverage xml --data-file=$coverageDataFile --omit=$coverageOmit --ignore-errors -o $coverageXmlFile

# Deactivate virtual environment
deactivate 
