# -*- coding: utf-8 -*-
#
# service_usage.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# Service API usage demonstration
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import sys
import time
import gom
import gom.api.services


SERVICE_NAME = "Reflector"
TIMEOUT = 30

def wait_for_status(service, status, timeout):
    """
    Wait for expected service status or timeout
    
    Args:
        service:  Service object
        status:   Expected status
        timeout:  Timeout in seconds

    Returns:
        Final status.

    """
    for _ in range(timeout):
        act_status = service.get_status()
        if act_status == status:
            break
        time.sleep(1)

    return service.get_status()


if __name__ == '__main__':
    print('Available services:')
    s_reflector = None
    for s in gom.api.services.get_services():
        print (s.get_name())
        if s.get_name() == SERVICE_NAME:
            srv = s
    print("\n")

    if not srv:
        print(f"Failed to get '{SERVICE_NAME}' service handle")
        sys.exit(0)

    print(f"'{srv.get_name()}' service properties")
    print(f"Autostart: {srv.get_autostart()}")
    print(f"Endpoint: {srv.get_endpoint()}")
    print(f"Number of instances: {srv.get_number_of_instances()}")
    print("\n")

    print(f"Attempting to change the '{srv.get_name()}' service status.")
    status = srv.get_status()
    print(f"Status: {status}")

    if status == "STOPPED":
        print("(Re-)Starting...", end="")
        srv.start()
        status = wait_for_status(srv, "RUNNING", TIMEOUT)
        print(status)

    print("Stopping...", end="")
    srv.stop()
    status = wait_for_status(srv, "STOPPED", TIMEOUT)
    print(status)

    print("Starting...", end="")
    srv.start()
    status = wait_for_status(srv, "RUNNING", TIMEOUT)
    print(status)

    import gom.api.math
    import gom.api.test

    # Call reflect function from service #2
    result = gom.api.test.reflect({'test': 123})
    print("gom.api.test.reflect({'test': 123}): " + f"{result}")

    # Call multiply function from service #1
    result = gom.api.math.multiply (23, 42)
    print(f"gom.api.math.multiply (23, 42): {result}")
