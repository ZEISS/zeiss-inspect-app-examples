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

> [!NOTE]
> For integration tests, the App under test must be set up in the ZEISS INSPECT App Explorer; either installed and in editing mode or in a connected folder.

> [!NOTE]
> The integration tests can be run via scripts/tests/run_integrationtests.py from the ZEISS INSPECT App Explorer or from a command line &ndash; Windows command prompt (`run_integrationtests.bat`) or PowerShell (`run_integrationtests.ps1`).

> [!NOTE]
> The unit tests are run from a command line &ndash; Windows command prompt (`run_unittests.bat`) or PowerShell (`run_unittests.ps1`).

> [!NOTE]
> A service "Pytest Reflector" is provided as an example by this App. It is used in the test case `test_service.py`.

> [!CAUTION]
> Pytest's test coverage does not include scripted elements and services, because those features are running in separate Python interpreter processes! However, test coverage for services can be obtained by applying the concept described in [Code Coverage for Services](#code-coverage-for-services). 

## App Contents

- `run_integrationtests.bat` - Script for running integration tests from Windows command prompt
- `run_integrationtests.ps1` - Script for running integration tests from Windows PowerShell
- `run_unittests.bat` - Script for running unit tests from Windows command prompt
- `run_unittests.ps1` - Script for running unit tests from Windows PowerShell
- `scripts/` - Scripts folder
   - `scripted_elements` - Scripted elements folder
      - `Scripted_Circle.py` - Scripted actual circle example
      - `Scripted_Circle.gdlg` - Dialog definition for scripted actual circle example
   - `services/` - Service scripts folder
      - `reflector.py` - Example service script
   - `uut_project_keywords.py` - Example (dummy) App as Unit Under Test (UUT)
   - `tests/` - Testcase folder
      - `test_integration` - Test group folder for integration tests (just as an example)
         - `test_blackbox.py` - Example testcase which treats the UUT as black box. It executes the UUT as script and checks the ZEISS INSPECT project for the expected changes of state afterwards (in this example: set project keywords).
         - `test_fail.py` - Dummy testcase which always fails
         - `test_dialog.py` - Example testcase for user-defined dialogs
         - `test_pass.py` - Dummy testcase which always passes
         - `test_scripted_element.py` - Example testcase for scripted elements
         - `test_service.py` - Example testcase for services
         - `test_whitebox.py` - Example testcase which calls the UUT function `get_project_keywords()` and checks its return value
      - `test_units` - Test group folder for unit tests (just as an example)
         - `test_units.py` - Unit testcase
      - `run_integrationtests.py` - Script for running all integration tests
      - `run_integrationtests_config.json` - Configuration file for `run_integrationtests.py`
      - `pytest_integrationtest_coverage.ini` - Default integration test configuration file for pytest
      - `run_unittests.py` - Script for running all unit tests
      - `run_unittests_config.json` - Configuration file for `run_unittests.py`
      - `pytest_unittests_coverage.ini` - Default unit test configuration file for pytest
      - `log/` - Default logfile folder
      - `reports/` - Default test report folder
        - `html/` - Test report in HTML format
        - `junit/` - Test report in JUnit XML format
        - `cov/` - Test coverage reports in HTML and XML format

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

To measure code coverage in services, a function decorator provided by `app_utils.service_coverage` is added to the service function to create/update the coverage report after each service function call. 

Example:

```
# Create instance of ServiceCoverage with specific coverage data file path
cover_reflect = ServiceCoverage(__file__)               # pragma: no cover

@apifunction          # Basic service function decorator
@cover_reflect.cover  # Coverage decorator
def reflect(value):
   ...
```

The ServiceCoverage decorator wraps the actual service function to start coverage before and to stop coverage and to write the data file after running the service function:

```
cov.start()
<service function>
cov.stop()
cov.save()
```

> [NOTE!]
> Coverage is only measured if the App's `metainfo.json` contains `"services-coverage": true` or if the ServiceCoverage attribute `cov_enabled` is set to `True`.

A separate coverage data file `.coverage.<pythonfile>` is generated for each service function.

Coverage data files of (multiple) services and the App itself can be merged using

```
$ coverage combine --data-file=./.coverage --keep scripts/services/ .coverage.pytest
```

Coverage reports can be created as follows:

```
$ coverage <report|html|xml|json|lcov> --data-file=./.coverage --omit=*/Local/Temp/*
```

For details see https://coverage.readthedocs.io/en/latest/cmd.html

## See also

* [Testing Apps](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/testing_apps/testing_apps.html)
* [Scripted elements](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/scripted_elements/scripted_elements_toc.html)
* [Using services](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/using_services/using_services.html)
