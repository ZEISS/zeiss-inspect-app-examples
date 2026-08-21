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

SERVICE_ENDPOINT = 'gom.api.pytest_template.reflect'

def test_reflect():
    """ Test a service """
    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if service.get_status() != 'RUNNING' and not service.start_and_wait():
        assert False, f"Failed to start service {SERVICE_ENDPOINT}"
    from gom.api.pytest_template.reflect import reflect  # pylint: disable=import-outside-toplevel, import-error  # pyright: ignore[reportMissingImports]
    assert reflect({"answer": 42}) == {"answer": 42}

def test_reflect2():
    """Test the reflect service (lazy import)"""
    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if service.get_status() != 'RUNNING' and not service.start_and_wait():
        assert False, f"Failed to start service {SERVICE_ENDPOINT}"
    assert gom.api.pytest_template.reflect.reflect({"answer": 42}) == {"answer": 42}
