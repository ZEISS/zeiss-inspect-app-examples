""" Integration test example for service

NOTE:
The test runner's pytest code coverage cannot include any services,
because they run in separate Python interpreter processes.

Instead, a dedicated coverage setup is used for services -
see services/reflector.py

Carl Zeiss GOM Metrology GmbH, 2026
"""

import gom
import gom.api.services
import time

SERVICE_ENDPOINT = 'gom.api.pytest_template.reflect'
SERVICE_TIMEOUT = 30000

# NOTE
# The service must be started before running the tests and
# stopped after the tests are completed to allow creation
# of coverage data files.
# The <service>.stop() method is asynchronous, so we need 
# to wait until the service actually stops.

def wait_until_stopped(service, timeout=SERVICE_TIMEOUT):
    """Wait until a service reaches the STOPPED state.

    Args:
        service: Service instance to monitor.
        timeout: Maximum wait time in milliseconds.

    Returns:
        True if the service stopped before the timeout, otherwise False.
    """
    deadline = time.monotonic() + timeout / 1000
    while time.monotonic() < deadline:
        if service.get_status() == 'STOPPED':
            return True
        time.sleep(0.1)
    return service.get_status() == 'STOPPED'

def test_reflect():
    """ Test a service """
    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if service.get_status() == 'RUNNING':
        service.stop()
        assert wait_until_stopped(service, SERVICE_TIMEOUT), f"Service {SERVICE_ENDPOINT} did not stop"

    if service.get_status() != 'RUNNING' and not service.start_and_wait(timeout=SERVICE_TIMEOUT):
        assert False, f"Failed to start service {SERVICE_ENDPOINT}"
    from gom.api.pytest_template.reflect import reflect  # pylint: disable=import-outside-toplevel, import-error  # pyright: ignore[reportMissingImports]
    assert reflect({"answer": 42}) == {"answer": 42}
    service.stop()
    assert wait_until_stopped(service, SERVICE_TIMEOUT), f"Service {SERVICE_ENDPOINT} did not stop"

def test_reflect2():
    """Test the reflect service (lazy import)"""
    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if service.get_status() == 'RUNNING':
        service.stop()
        assert wait_until_stopped(service, SERVICE_TIMEOUT), f"Service {SERVICE_ENDPOINT} did not stop"
    if service.get_status() != 'RUNNING' and not service.start_and_wait(timeout=SERVICE_TIMEOUT):
        assert False, f"Failed to start service {SERVICE_ENDPOINT}"
    assert gom.api.pytest_template.reflect.reflect({"answer": 42}) == {"answer": 42}
    service.stop()
    assert wait_until_stopped(service, SERVICE_TIMEOUT), f"Service {SERVICE_ENDPOINT} did not stop"
