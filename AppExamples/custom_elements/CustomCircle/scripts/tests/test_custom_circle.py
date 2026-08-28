"""
Test for custom circle element
"""

import gom
import gom.api.services

SERVICE_ENDPOINT = 'gom.api.examples.custom_circle'
SERVICE_TIMEOUT = 10000

CENTER_X = 10.0
CENTER_Y = 20.0
CENTER_Z = 30.0
DIR_X = 0.0
DIR_Y = 0.0
DIR_Z = 1.0
RADIUS = 50.0


def test_actual_circle():
    """Test custom actual circle element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Circle"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_circle',
        name=name,
        values={
            'center_x': CENTER_X, 'center_y': CENTER_Y, 'center_z': CENTER_Z,
            'dir_x': DIR_X, 'dir_y': DIR_Y, 'dir_z': DIR_Z,
            'radius': RADIUS
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    assert elem.center_coordinate.x == CENTER_X
    assert elem.center_coordinate.y == CENTER_Y
    assert elem.center_coordinate.z == CENTER_Z
    assert elem.diameter / 2.0 == RADIUS
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.center_x == CENTER_X
    assert elem.center_y == CENTER_Y
    assert elem.center_z == CENTER_Z


def test_nominal_circle():
    """Test custom nominal circle element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Circle"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_circle',
        name=name,
        values={
            'center_x': CENTER_X, 'center_y': CENTER_Y, 'center_z': CENTER_Z,
            'dir_x': DIR_X, 'dir_y': DIR_Y, 'dir_z': DIR_Z,
            'radius': RADIUS
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.nominal_elements[name]
    assert elem.center_coordinate.x == CENTER_X
    assert elem.center_coordinate.y == CENTER_Y
    assert elem.center_coordinate.z == CENTER_Z
    assert elem.diameter / 2.0 == RADIUS
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.center_x == CENTER_X
    assert elem.center_y == CENTER_Y
    assert elem.center_z == CENTER_Z
