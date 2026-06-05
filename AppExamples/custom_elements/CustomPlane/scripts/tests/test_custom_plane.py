"""
Test for custom plane element
"""

import gom
import gom.api.services
import math

SERVICE_ENDPOINT = 'gom.api.examples.custom_plane'
SERVICE_TIMEOUT = 10000

NORMAL_X = 0.0
NORMAL_Y = 0.0
NORMAL_Z = 1.0
POINT_X = 0.0
POINT_Y = 0.0
POINT_Z = 50.0
# Expected nominal distance = dot(normal, point)
EXPECTED_DISTANCE = NORMAL_X * POINT_X + NORMAL_Y * POINT_Y + NORMAL_Z * POINT_Z


def test_actual_plane():
    """Test custom actual plane element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Plane"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_plane',
        name=name,
        values={
            'normal_x': NORMAL_X, 'normal_y': NORMAL_Y, 'normal_z': NORMAL_Z,
            'point_x': POINT_X, 'point_y': POINT_Y, 'point_z': POINT_Z
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.normal_x == NORMAL_X
    assert elem.normal_y == NORMAL_Y
    assert elem.normal_z == NORMAL_Z


def test_nominal_plane():
    """Test custom nominal plane element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Plane"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_plane',
        name=name,
        values={
            'normal_x': NORMAL_X, 'normal_y': NORMAL_Y, 'normal_z': NORMAL_Z,
            'point_x': POINT_X, 'point_y': POINT_Y, 'point_z': POINT_Z
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.nominal_elements[name]
    assert math.isclose(elem.distance_from_origin, EXPECTED_DISTANCE)
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.normal_x == NORMAL_X
    assert elem.normal_y == NORMAL_Y
    assert elem.normal_z == NORMAL_Z
