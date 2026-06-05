"""
Test for custom value element
"""

import gom
import gom.api.services

SERVICE_ENDPOINT = 'gom.api.examples.custom_value_element'
SERVICE_TIMEOUT = 10000

VALUE = 7.0
# Expected custom data: value_squared = VALUE * VALUE
EXPECTED_VALUE_SQUARED = VALUE * VALUE


def test_actual_value_element():
    """Test custom actual value element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Value Element"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_value_element',
        name=name,
        values={'value': VALUE}
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    assert elem.dimension == VALUE
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.value_squared == EXPECTED_VALUE_SQUARED


def test_nominal_value_element():
    """Test custom nominal value element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Value Element"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_value_element',
        name=name,
        values={'value': VALUE}
    )

    #
    # TEST
    #
    elem = gom.app.project.nominal_elements[name]
    assert elem.dimension == VALUE
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.value_squared == EXPECTED_VALUE_SQUARED
