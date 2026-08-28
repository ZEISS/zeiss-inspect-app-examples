"""
Test for custom cylinder element
"""

import gom
import gom.api.services

SERVICE_ENDPOINT = 'gom.api.examples.custom_cylinder'
SERVICE_TIMEOUT = 10000

CENTER_X = 5.0
CENTER_Y = 10.0
CENTER_Z = 15.0
DIR_X = 0.0
DIR_Y = 1.0
DIR_Z = 0.0
RADIUS = 25.0


def test_actual_cylinder():
    """Test custom actual cylinder element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Cylinder"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_cylinder',
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
    assert elem.coordinate1.x == CENTER_X
    assert elem.coordinate1.y == CENTER_Y
    assert elem.coordinate1.z == CENTER_Z
    assert elem.direction.x == DIR_X
    assert elem.direction.y == DIR_Y
    assert elem.direction.z == DIR_Z
    assert elem.diameter == RADIUS * 2
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.center_x == CENTER_X
    assert elem.center_y == CENTER_Y
    assert elem.center_z == CENTER_Z


def test_nominal_cylinder():
    """Test custom nominal cylinder element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Cylinder"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_cylinder',
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
    assert elem.coordinate1.x == CENTER_X
    assert elem.coordinate1.y == CENTER_Y
    assert elem.coordinate1.z == CENTER_Z
    assert elem.direction.x == DIR_X
    assert elem.direction.y == DIR_Y
    assert elem.direction.z == DIR_Z
    assert elem.diameter == RADIUS * 2
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.center_x == CENTER_X
    assert elem.center_y == CENTER_Y
    assert elem.center_z == CENTER_Z
