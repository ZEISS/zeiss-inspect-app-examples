# PytestTemplate

Template for App integration testing using pytest

Generates test reports and test coverage reports.

Python package requirements:
* [pytest](https://pypi.org/project/pytest/)
* [pytest-cov](https://pypi.org/project/pytest-cov/)
* [pytest-html](https://pypi.org/project/pytest-html/)

## Notes

> [!NOTE]
> The App under test must be set up in the ZEISS INSPECT App explorer; either installed and in editing mode or in a connected folder.

> [!NOTE]
> The tests can be run via scripts/tests/testrunner.py from the ZEISS INSPECT App Explorer or from a command line &ndash; Windows command prompt (`run_tests.bat`) or PowerShell (`run_tests.ps1`).

## App Contents

- `run_tests.bat` - Script for running tests from Windows command prompt
- `run_tests.ps1` - Script for running tests from Windows PowerShell
- `scripts/` - Scripts folder
   - `uut_project_keywords.py` - Example Unit Under Test (UUT)
   - `tests/` - Test case folder
      - `test_blackbox.py` - Example test case which treats the UUT as black box. It executes the UUT as script and checks the ZEISS INSPECT project for the expected changes of state afterwards (in this example: set project keywords).
      - `test_fail.py` - Dummy testcase which always fails
      - `test_pass.py` - Dummy testcase which always passes
      - `test_whitebox.py` - Example testcase which calls the UUT function `get_project_keywords()` and checks its return value
      - `testrunner.py` - Script for running all tests
      - `testrunner_config.json` - Configuration file for testrunner.py
      - `pytest_integrationtest_coverage.cfg` - Default pytest configuration file
      - `log/` - Default logfile folder
      - `reports/` - Default test report folder
        - `html/` - Test report in HTML format
        - `junit/` - Test report in JUnit XML format
        - `cov/` - Test coverage reports in HTML and XML format

## Configuration

### Testrunner

`testrunner_config.json`

* `pytest_cfg` - pytest configuration file (in `scripts/tests/`, default: `pytest_integrationtest_coverage.cfg`)
* `pytest_log_dir` - Testrunner logfile directory (relative to `scripts/tests/` or absolute path; default: `log`)
* `reports_dir` - Test reports reports directory (relative to `scripts/tests/` or absolute path; default: `reports`)

### pytest

Default file defined in `tests/testrunner_config.json`: `pytest_integrationtest_coverage.cfg`

* Coverage target(s) (default: `uut_project_keywords`)
* pytest cache directory (default: `scripts/tests/.pytest_cache`)
* Report files

See [pytest documentation](https://pytest-html.readthedocs.io/en/latest/) for details.

## See also

See https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/testing_apps/testing_apps.html for more information.
