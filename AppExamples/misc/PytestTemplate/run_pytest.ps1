# Runs the PytestTemplate integration tests against a running ZEISS INSPECT instance.
#
# Creates and activates a virtual environment, configures the ZEISS INSPECT
# Python API connection, installs the API wheel and pytest, and executes the
# tests in scripts/tests.
#
# Requires ZEISS INSPECT >= 2027.
#
# Carl Zeiss GOM Metrology GmbH, 2026
# ------------------------------------------------------------------------------------------------

# ZEISS INSPECT version
$zixVersion = 2027

# Python executable path
$pythonExe = "$env:LOCALAPPDATA\Programs\Python\Python314\python.exe"
if (-not (Test-Path -LiteralPath $pythonExe -PathType Leaf)) {
	throw "Python executable was not found at $pythonExe. Update the path defined by `$pythonExe`."
}

$inspectDir = "C:\Program Files\Zeiss\INSPECT\$zixVersion"

#
# Check if ZEISS INSPECT is running
#
$inspectProcesses = @(Get-CimInstance Win32_Process -Filter "Name = 'ZEISS_INSPECT.exe'")
if ($inspectProcesses.Count -eq 0) {
	throw "ZEISS INSPECT $zixVersion is not running."
}
$inspectExe = $inspectProcesses[0].ExecutablePath
Write-Host "ZEISS INSPECT is running at: $inspectExe"

#
# Get the ZEISS INSPECT API port and key from the gomsoftware.cfg file
#
$configPath = "$env:APPDATA\gom\$zixVersion\gomsoftware.cfg"
$apiConfigurationLine = Get-Content $configPath | Where-Object { $_ -match '^\s*ApiConfiguration\s*=' } | Select-Object -First 1
if (-not $apiConfigurationLine) {
	throw "ApiConfiguration was not found in $configPath."
}
$apiConfiguration = ($apiConfigurationLine -replace '^\s*ApiConfiguration\s*=\s*', '') -split '\s+'
if ($apiConfiguration.Count -lt 6) {
	throw "ApiConfiguration in $configPath does not contain an API port and key."
}
$apiPort = [int]$apiConfiguration[3]
$apiKey = $apiConfiguration[5]
Write-Host "ZEISS INSPECT API port is: $apiPort"
#Write-Host "ZEISS INSPECT API key is: $apiKey"

#
# Configure the ZEISS INSPECT Python API connection
#
$env:TOM_PYTHON_API_URL = "ws://localhost:$apiPort/?apikey=$apiKey"

#
# Create and activate a virtual Python environment
#
& $pythonExe -m venv .venv
.\.venv\Scripts\Activate.ps1

#
# Install the ZEISS INSPECT API wheel and pytest in the virtual environment
# and set PYTHONPATH to include the ZEISS INSPECT Python API modules
#
$inspectPythonPaths = @(
	"$inspectDir\lib\python\gom-python"
	"$inspectDir\lib\python\internal"
)
if ($env:PYTHONPATH) {
	$inspectPythonPaths += $env:PYTHONPATH
}
$env:PYTHONPATH = $inspectPythonPaths -join [IO.Path]::PathSeparator

python -m pip install --quiet --upgrade pip

$wheel = Get-ChildItem -Path "$inspectDir\wheels" -Filter "zeiss_inspect_api-*.whl" | Select-Object -First 1
if (-not $wheel) {
	throw "No wheel matching zeiss_inspect_api-*.whl was found in $inspectDir\wheels."
}
python -m pip install --quiet $wheel.FullName
python -m pip install --quiet pytest pytest-cov

#
# Remove any existing pytest and service coverage data before running the tests
#
Remove-Item -LiteralPath ".coverage" -ErrorAction SilentlyContinue
Remove-Item -LiteralPath ".coverage.pytest" -ErrorAction SilentlyContinue
Remove-Item -LiteralPath "scripts\tests\.coverage" -ErrorAction SilentlyContinue
$serviceCoverageFiles = Get-ChildItem -Path "cov_temp" -Filter ".coverage.*" -File -Force -ErrorAction SilentlyContinue
$serviceCoverageFiles | Remove-Item -Force -ErrorAction SilentlyContinue

#
# Run the tests in scripts/tests, eventually using the ZEISS INSPECT API connection
#
$currentPath = Get-Location
try {
	Set-Location -Path "scripts/tests"
	pytest -c pytest_integrationtest_coverage.ini
}
finally {
	Set-Location -Path $currentPath
}

# Preserve pytest's coverage data for combining with service coverage data.
if (Test-Path -LiteralPath "scripts\tests\.coverage" -PathType Leaf) {
	Copy-Item -LiteralPath "scripts\tests\.coverage" -Destination "cov_temp\.coverage.pytest" -ErrorAction SilentlyContinue
}

#
# Deactivate virtual environment
#
deactivate

. ".\report_coverage.ps1"