# ---
# service_manager.py
#
# Utility for starting ZEISS INSPECT services
#
# Carl Zeiss GOM Metrology GmbH, 2025
# ---

import gom
import time
import gom.api.services

class ServiceManager:
    def __init__(self, name, endpoint = "", stop = True, timeout_sec = 30):
        """ServiceManager
        Example:
        >>> def test_myservice():
        >>>    with ServiceManager("Multiplicator", "gom.api.foo"):
        >>>        import gom.api.foo
        >>>        assert gom.api.foo.multiply(6, 7) == 42
        Args:
            name (str):         Service name
            endpoint (str):     Service endpoint
            stop (bool):        If True, stop service on exit.
            timeout_sec (int):  Timeout in seconds

        Raises:
            NameError: Service with expected name (and optional endpoint) was not found.
        """
        self.stop = stop
        self.srv = None
        self.timeout_sec = timeout_sec

        for s in gom.api.services.get_services():
            if s.get_name() == name:
                if not endpoint or s.get_endpoint() == endpoint:
                    self.srv = s
                    return
        if self.srv is None:
            raise NameError("Service not found.")

    def __enter__(self):
        """Start service if it is not running.
        Returns:
            gom.api.services.Service: Service handle

        Raises:
            TimeoutError: Timeout occurred before service reached expected status.
        """
        if self.srv.get_status() != "RUNNING":
            self.srv.start()
            self.wait_for_status("RUNNING")

        return self.srv

    def __exit__(self, exc_type, exc_value, traceback):
        """Stop service if required."""
        if self.stop and self.srv.get_status() == "RUNNING":
            self.srv.stop()

    def wait_for_status(self, status):
        """Wait for expected service status or timeout

        Args:
            status: Expected status

        Raises:
            TimeoutError: Timeout occurred before service reached expected status.
        """
        for _ in range(self.timeout_sec):
            if self.srv.get_status() == status:
                return
            time.sleep(1)
        raise TimeoutError("Timeout starting service.")
