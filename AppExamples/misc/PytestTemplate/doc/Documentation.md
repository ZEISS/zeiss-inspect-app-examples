# PytestTemplate

Template for App integration testing and unit testing using pytest

Generates test reports and test coverage reports.

* **Integration testing**: Test cases are running in ZEISS INSPECT
* **Unit testing**: Test cases are running in standalone Python interpreter

Python package requirements:
* [pytest](https://pypi.org/project/pytest/)
* [pytest-cov](https://pypi.org/project/pytest-cov/)
* [pytest-html](https://pypi.org/project/pytest-html/)
* [pytest-xdist](https://pypi.org/project/pytest-xdist/)

## Notes

For integration tests, the App under test must be set up in the ZEISS INSPECT App Explorer. It must either be installed and in editing mode or be available in a connected folder.

There are two ways to run the integration tests from a command line:

- `run_integrationtests.ps1` (PowerShell) and `run_integrationtests.bat` (Windows command prompt) start ZEISS INSPECT, run the in-application test runner for the configured software versions, and combine the coverage data from pytest and services. The PowerShell script is the preferred option.
- `run_pytest.ps1` runs pytest directly against an already running ZEISS INSPECT instance. It creates the virtual environment, installs the ZEISS INSPECT API and pytest, and runs the tests for that instance. This workflow is closer to common Python frameworks because it invokes pytest directly and does not require a ZEISS INSPECT-side testrunner. Use it for a quick direct run when ZEISS INSPECT is already open; it does not start ZEISS INSPECT or run the multi-version coverage combination performed by the other integration-test scripts.

The integration tests can also be started from the ZEISS INSPECT App Explorer by running `scripts/tests/run_integrationtests.py`.

Unit tests run from a command line using the Windows command prompt script (`run_unittests.bat`) or the PowerShell script (`run_unittests.ps1`).

The service "Pytest Reflector" is provided as an example and is used by `test_service.py`.

> [!CAUTION]
> Pytest's test coverage does not include scripted elements and services, because those features are running in separate Python interpreter processes! However, test coverage for services can be obtained by applying the concept described in [Code Coverage for Services](#code-coverage-for-services). 

## App Contents

- `metainfo.json` - App metadata and configuration
- `run_integrationtests.bat` - Runs integration tests from Windows Command Prompt
- `run_integrationtests.ps1` - Runs integration tests from PowerShell
- `run_pytest.ps1` - Runs integration tests directly against a running ZEISS INSPECT instance
- `run_unittests.bat` - Runs unit tests from Windows Command Prompt
- `run_unittests.ps1` - Runs unit tests from PowerShell
- `run_script.ps1` - Runs a Python script from an external interpreter in ZEISS INSPECT
- `report_coverage.ps1` - Generates the combined coverage report
- `doc/` - App documentation
   - `Documentation.md` - This documentation
   - `README.md` - App overview
   - `Releasenotes.md` - App release notes
   - `Releasenotes.pdf` - App release notes in PDF format
- `license/` - App license information
   - `license.txt` - License text
- `scripts/` - App scripts and tests
   - `dialog.gdlg` - Dialog definition used by the tests
   - `my_script.py` - Minimal script to test the ZEISS INSPECT Python API connection
   - `uut_project_keywords.py` - Example Unit Under Test (UUT)
   - `app_utils/` - App utilities
      - `service_coverage.py` - Service coverage support
   - `custom_elements/` - Custom element scripts used by the tests
      - `Custom_Circle.gdlg` - Custom circle dialog definition
      - `Custom_Circle.py` - Custom circle implementation
   - `modules/` - Python package requirements and wheelhouse
      - `requirements.txt` - Python package requirements
   - `scripted_elements/` - Scripted element scripts used by the tests
      - `Scripted_Circle.gdlg` - Scripted circle dialog definition
      - `Scripted_Circle.py` - Scripted circle implementation
   - `services/` - Service scripts used by the tests
      - `multiply.py` - Multiply service implementation
      - `reflector.py` - Reflector service implementation
   - `tests/` - Test cases, test runners, and configurations
      - `pytest_integrationtest_coverage.ini` - Integration-test pytest configuration
      - `pytest_unittest_coverage.ini` - Unit-test pytest configuration
      - `run_integrationtests_config.json` - Integration-test runner configuration
      - `run_integrationtests.py` - Integration-test runner
      - `run_unittests_config.json` - Unit-test runner configuration
      - `run_unittests.py` - Unit-test runner
      - `test_integration/` - Integration test cases
         - `test_blackbox.py` - Black-box test (intentionally failing)
         - `test_custom_circle.py` - Custom circle element test
         - `test_dialog.py` - Dialog test
         - `test_fail.py` - Intentionally failing example test
         - `test_pass.py` - Passing example test
         - `test_scripted_element.py` - Legacy scripted element test
         - `test_service.py` - Service test
         - `test_whitebox.py` - White-box test
      - `test_units/` - Unit test cases
         - `test_units.py` - Unit test example

## Configuration

### Integration Tests

#### Testrunner

`run_integrationtests_config.json`

* `pytest_cfg` - pytest configuration file (in `scripts/tests/`, default: `pytest_integrationtest_coverage.ini`)
* `pytest_log_dir` - Testrunner logfile directory (relative to `scripts/tests/` or absolute path; default: `log`)
* `reports_dir` - Test reports directory (relative to `scripts/tests/` or absolute path; default: `reports`)

#### pytest

Default file defined in `tests/run_integrationtests_config.json`: `pytest_integrationtest_coverage.ini`

* Coverage target(s) (default: `uut_project_keywords`)
* pytest cache directory (default: `scripts/tests/.pytest_cache`)

See [pytest documentation](https://pytest-html.readthedocs.io/en/latest/) for more.

### Unit Tests

#### Testrunner

`run_unittests_config.json`

* `pytest_cfg` - pytest configuration file (in `scripts/tests`, default: `pytest_unittest_coverage.ini`)
* `reports_dir` -  Test reports directory (relative to `scripts/tests/` or absolute path; default: `reports`)

#### pytest

Default file defined in `tests/run_unittests_config.json`: `pytest_unittest_coverage.ini`

* Coverage target(s) (default: `uut_project_keywords`)
* pytest cache directory (default: `scripts/tests/.pytest_cache`)
* Number of parallel worker processes (default: not used)

See [pytest documentation](https://pytest-html.readthedocs.io/en/latest/) and 
[pytest-xdist documentation](https://pytest-xdist.readthedocs.io/en/stable/) for more.

## Code Coverage for Services

Services run in separate Python interpreter processes, so their execution is not included in the coverage data collected by pytest. The `app_utils.service_coverage` module provides a `@coverage` decorator that records coverage for a service function and saves the data after each call.

Enable service coverage by adding `"services-coverage": true` to the App's `metainfo.json`. Without this setting, the decorator leaves the service function unchanged and no service coverage data is written.

Add the decorator below the `@apifunction` decorator:

```
@apifunction
@coverage
def reflect(value):
   return value
```

For each decorated service, coverage data is written to the App's `cov_temp` directory as `.coverage.<service_module>`. The data is saved in a `finally` block, so it is written when the service function returns or raises an exception.

The integration-test scripts copy pytest coverage data to `cov_temp` and combine it with the service data. To combine existing data and generate the final reports manually, run `report_coverage.ps1` from the App root:

```powershell
.\report_coverage.ps1
```

The combined HTML report is generated under `scripts/tests/reports/cov/html_combined`, and the combined XML report is written to `scripts/tests/reports/cov/integrationtest-combined-coverage.xml`.

## See also

* [Testing Apps](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/testing_apps/testing_apps.html)
* [Scripted elements](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_elements_toc.html)
* [Using services](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/using_services/using_services.html)
