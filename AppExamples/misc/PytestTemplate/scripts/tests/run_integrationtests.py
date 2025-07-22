"""App test runner using pytest ()

Runs all test cases in the App's scripts/tests/ folder and its subfolders.
see https://docs.pytest.org/

Carl Zeiss GOM Metrology GmbH, 2025
"""

import gom
import sys
import os
import json
import pytest
from datetime import datetime

VERSION = gom.app.application_build_information.version.split()[0]

class PseudoTTY:
    """Patch for terminal output in ZEISS INSPECT
    """
    def __init__(self, underlying):
        self.__underlying = underlying

    def __getattr__(self, name):
        return getattr(self.__underlying, name)

    def isatty(self):
        """Pretend to be a TTY"""
        return True

    def write(self, message):
        """Write the message to the underlying stream (file)"""
        self.__underlying.write(message)

    def flush(self):
        """Ensure that the underlying stream is flushed"""
        self.__underlying.flush()

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
    print(f'ZEISS INSPECT {VERSION} Testrunner Logfile, created {timestamp}\n')

    # Get test case folder
    tests_path = os.path.dirname(os.path.abspath(__file__))
    print(f'Test case folder: {tests_path}\n')

    print(f'{sys.path=}\n')

    reports_path = config['reports_dir']
    if not os.path.exists(reports_path):
        reports_path = os.path.join(tests_path, reports_path)

    junit_path = os.path.join(reports_path, "junit", f"integration-test-sw{VERSION}-results.xml")
    html_path =  os.path.join(reports_path, "html", f"integration-test-sw{VERSION}-results.html")

    cov_path = os.path.join(reports_path, 'cov')
    if not os.path.exists(cov_path):
        try:
            os.mkdir(cov_path)
        except Exception as e:
            print(f"An error occurred: {e}")

    os.chdir(cov_path)

    pytest_args = [
        f"{tests_path}", 
        "--color", "no", 
        "-vv", 
        "--durations", "0", 
        "--junitxml", f"{junit_path}",
        "--html", f"{html_path}",
        "--cov-report", f"html:{os.path.join(cov_path, 'integrationtest-coverage')}",
        "--cov-report", f"xml:{os.path.join(cov_path, 'integrationtest-coverage.xml')}"
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
    print(f"Coverage Report: file://{cov_path}/integrationtest-coverage/index.html")
    return rv

if __name__ == "__main__":
    addon = gom.api.addons.get_current_addon()
    is_finalized = addon.get_file().endswith('.addon')
    assert not is_finalized, "ERROR: App must be in editing mode or in connected folder!"

    gom.script.sys.update_addon_database()
    scripts_dir = get_scripts_path()

    test_config = read_config(os.path.join(scripts_dir, "tests", "integrationtests_config.json"))

    if 'pytest_log_dir' in test_config:
        log_path = test_config['pytest_log_dir']
        if not os.path.exists(log_path):
            log_path = os.path.join(scripts_dir, 'tests', log_path)
        assert os.access(log_path, os.W_OK), "ERROR: Log directory is not writable!"
        log_path = os.path.join(log_path, f"pytest_sw{VERSION}.log")
        print(f"See {log_path}") 
        with open(os.path.join(log_path), 'w', encoding='cp437') as f:
            sys.stdout = PseudoTTY(f)
            sys.stderr = PseudoTTY(f)
            prepare_sys_path(scripts_dir)
            main(test_config)
    else:
        sys.stdout = PseudoTTY(sys.stdout)
        main(test_config)

    # Catch exception in case the script was started from the App Editor
    try:
        # Works with ZEISS INSPECT SW2025 and newer
        gom.script.sys.exit_program (0)
    except gom.RequestError:
        pass
