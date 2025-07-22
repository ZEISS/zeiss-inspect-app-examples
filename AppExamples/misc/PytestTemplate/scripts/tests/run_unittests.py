import sys
import os
import json
import pytest
from datetime import datetime

class MockGom:
    """Define a mock version of the 'gom' module

    This allows to import a unit-under-test into unit test cases,
    even if it contains an 'import gom' command.
    Provide any functions or attributes that the UUT expects, but
    where the functionality is actually not needed for unit tests.
    """
    def mock_function(self):
        """Dummy method"""
        return "This is a mock function."

    def run_function(self, original_function):
        """run_function() is required by ZEISS INSPECT test runner"""
        def wrapped_function(*args, **kwargs):
            # Log the function name and arguments
            #print(f"Calling function: {original_function.__name__}")
            #print(f"Arguments: {args}, {kwargs}")

            # Call the original function
            result = original_function(*args, **kwargs)

            # Optionally log the result
            #print(f"Result: {result}")

            return result
        return wrapped_function

def read_config(file_path):
    """Read configuration values from a JSON file."""
    _config = []
    try:
        with open(file_path, 'r', encoding='utf-8') as config_file:
            _config = json.load(config_file)  # Parse the JSON data
    except FileNotFoundError:
        pass

    return _config

def get_scripts_path():
    """Get the App's scripts/ path
    """
    scripts_path = os.path.abspath(__file__)
    while os.path.basename(scripts_path) != "scripts":
        scripts_path = os.path.dirname(scripts_path)
    return scripts_path

def prepare_sys_path(scripts_path):
    """Add directory tree starting from <App>/scripts to sys.path
    
    This allows to import any Python file within the App as module.
    """
    sys.path.append(scripts_path)

    skip_paths = []
    for d in ["modules", "tests"]:
        skip_paths.append(os.path.join(scripts_path, d))

    for root, dirs, _ in os.walk(scripts_path):
        skip = False
        for p in skip_paths:
            if root.find(p) != -1:
                skip = True
        if skip:
            continue

        for my_dir in dirs:
            full_path = os.path.join(root, my_dir)
            if not full_path in skip_paths:
                sys.path.append(full_path)

def main(config):
    '''Run tests and generate coverage report'''

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Unit Test Runner Logfile, created {timestamp}\n')

    # Get test case folder
    tests_path = os.path.dirname(os.path.abspath(__file__))
    print(f'Test case folder: {tests_path}\n')

    print(f'{sys.path=}\n')

    reports_path = config['reports_dir']
    if not os.path.exists(reports_path):
        reports_path = os.path.join(tests_path, reports_path)

    junit_path = os.path.join(reports_path, "junit", "unit-test-results.xml")
    html_path =  os.path.join(reports_path, "html", "unit-test-results.html")

    cov_path = os.path.join(reports_path, 'cov')
    if not os.path.exists(cov_path):
        try:
            os.mkdir(cov_path)
        except Exception as e:
            print(f"An error occurred: {e}")

    #os.chdir(cov_path)

    pytest_args = [
        f"{tests_path}", 
        "--color", "no", 
        "-vv", 
        "--durations", "0", 
        "--junitxml", f"{junit_path}",
        "--html", f"{html_path}",
        "--cov-report", f"html:{os.path.join(cov_path, 'unittest-coverage')}",
        "--cov-report", f"xml:{os.path.join(cov_path, 'unittest-coverage.xml')}"
    ]

    if 'pytest_cfg' in config and config['pytest_cfg']:
        config_path = os.path.join(tests_path, config['pytest_cfg'])
        pytest_args = ["--config-file", f"{config_path}"] + pytest_args
        print(f"{pytest_args=}")

    # See https://docs.pytest.org/en/stable/reference/reference.html#command-line-flags
    # Notes:
    # Coverage is enabled and configured in the pytest configuration file!
    # Additional coverage parameters are set in .coveragerc
    rv = pytest.main(pytest_args)

    print('\n')
    print(f"Test Report: file://{html_path}")
    print(f"Coverage Report: file://{cov_path}/unittest-coverage/index.html")
    return rv

if __name__ == "__main__":
    scripts_dir = get_scripts_path()

    test_config = read_config(os.path.join(scripts_dir, "tests", "run_unittests_config.json"))

    prepare_sys_path(scripts_dir)

    # Add the mock gom module to sys.modules
    sys.modules['gom'] = MockGom()

    main(test_config)
