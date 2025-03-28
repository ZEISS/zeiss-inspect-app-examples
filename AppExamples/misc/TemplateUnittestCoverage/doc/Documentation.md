# TemplateUnittestCoverage

Template for unit testing and generating a test coverage report

Based on `unitest` (https://docs.python.org/3/library/unittest.html) and `Coverage.py` (https://coverage.readthedocs.io/)

## Notes

> [!NOTE]
> The Python package `coverage` must be installed via the Add-on Explorer. 

> [!NOTE]
> The Add-on must be in editing mode to run the tests.


## File contents
- `uut_project_keywords.py` - Example Unit Under Test (UUT)
- `tests/` - Test case folder
   - `test_blackbox.py` - Example test case which treats the UUT as black box. It executes the UUT as script and checks the ZEISS INSPECT project for the expected changes of state afterwards (in this example: set project keywords).
   - ` test_fail.py` - Dummy testcase which always fails.
   - `test_pass.py` - Dummy testcase which always passes.
   - `test_whitebox.py` - Example testcase which calls the UUT function `get_project_keywords()` and checks its return value
- `run_tests.py` - Script for running all unit tests and generating the coverage report.

## See also

See https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/testing_apps/testing_apps.html for more information.
