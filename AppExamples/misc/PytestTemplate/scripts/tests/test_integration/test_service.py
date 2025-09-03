""" Integration test example for service

NOTE:
The test runner's pytest code coverage cannot include any services,
because they run in separate Python interpreter processes.

Instead, a dedicated coverage setup is used for services -
see services/reflector.py

Carl Zeiss GOM Metrology GmbH, 2025
"""

import gom
import time
import gom.api.services
from app_utils.service_manager import ServiceManager
    
def test_reflect():
    """ Test a service
    
    The ServiceManager context manager starts and stops the service,
    which is especially useful if the App is not installed, but used
    from a connected folder. 
    """
    
    with ServiceManager("Pytest Reflector"):
        from gom.api.pytest_template.reflect import reflect

        assert reflect({"answer": 42}) == {"answer": 42}
