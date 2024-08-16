# ServiceExample

## Short description

This example demonstrates how to implement, use and manage services.

## Highlights

### 1. Service implementation

The service API function has the `@apifunction` decorator and the service script calls `gom.run_api()`:

**Service script example `multiplicator/service.py`**

```python
import gom
from gom import apifunction

@apifunction
def multiply(value1: float, value2: float) -> float:
	gom.log.debug('Function "multiply" called')
	return value1 * value2
	
gom.run_api()
```

The service is configured in the App's `metainfo.json`:

```json
{
    "services": [
        {
            "endpoint": "gom.api.math",
            "name": "Multiplicator",
            "script": "multiplicator/service.py"
        }
    ],
}
```

### 2. Service usage

The service must be installed and started before it can be used. To use a service in a script, import its API endpoint and call its API function:

**Example script using the multiply() function provided by the multiplicator service with endpoint `gom.api.math`:**

```python
import gom.api.math

result = gom.api.math.multiply (24, 7)
print(result)
```

### 3. Service management from a script

[gom.api.services](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/python_api.html#gom-api-services) allows to query and control services from a script:

**Example script for querying and controlling services:**

```python
import sys
import time
import gom.api.services

SERVICE_NAME = "Reflector"
TIMEOUT = 30

# Wait for expected status or timeout
def wait_for_status(service, status, timeout):
    for _ in range(timeout):
        act_status = service.get_status()
        if act_status == status:
            break
        time.sleep(1)

    return service.get_status()

# Find service handle by name
srv = None
for s in gom.api.services.get_services():
	if s.get_name() == SERVICE_NAME:
		srv = s

if not srv:
	print("Failed to get {SERVICE_NAME} service handle")
   sys.exit(0)

# Query service properties
print(f"'{srv.get_name()}' service properties")
print(f"Autostart: {srv.get_autostart()}")
print(f"Endpoint: {srv.get_endpoint()}")
print(f"Number of instances: {srv.get_number_of_instances()}")

# Control service
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
```

## Related

* How-to: [Using services](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/using_services/using_services.html)
* [gom.api.services](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/python_api.html#gom-api-services)
