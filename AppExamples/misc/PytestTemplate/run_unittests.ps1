###############################################################################
# run_unittests.ps1 - Run ZEISS INSPECT App unit tests from Windows PowerShell
#
#
# * Uses 
#   * pytest
#   * pytest-cov
#   * pytest-html
#   * pytest-xdist
#   -- install with initial run (see below)
# * Set zixVersion to the ZEISS INSPECT version to select the Python interpreter
# * See doc/ for more information.
###############################################################################

$zixVersion = 2025
$pythonExe = "C:\Program Files\Zeiss\INSPECT\$zixVersion\python\python.exe"

# Comment out the following line to reduce startup time
& $pythonExe -m pip install -r scripts/modules/requirements.txt

& $pythonExe .\scripts\tests\run_unittests.py
