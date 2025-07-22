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
# * See scripts/tests/log/ for logfiles.
# * See doc/ for more information.
###############################################################################

$zixVersion = 2025
$pythonExe = "C:\Program Files\Zeiss\INSPECT\$zixVersion\python\python.exe"

# Uncomment the following lines to install pytest and its
# required submodules with initial run
#& $pythonExe -m pip install pytest
#& $pythonExe -m pip install pytest-cov
#& $pythonExe -m pip install pytest-html
#& $pythonExe -m pip install pytest-xdist

& $pythonExe .\scripts\tests\run_unittests.py
