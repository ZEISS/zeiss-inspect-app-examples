"""
Test for custom distance element
"""

import gom
import gom.api.services
import math

SERVICE_ENDPOINT = 'gom.api.examples.custom_distance'
SERVICE_TIMEOUT = 10000

P1_X = 0.0
P1_Y = 0.0
P1_Z = 0.0
P2_X = 3.0
P2_Y = 4.0
P2_Z = 0.0
EXPECTED_DISTANCE = math.sqrt(
    (P2_X - P1_X) ** 2 + (P2_Y - P1_Y) ** 2 + (P2_Z - P1_Z) ** 2
)


def test_actual_distance():
    """Test custom actual distance element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Distance"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_distance',
        name=name,
        values={
            'p1_x': P1_X, 'p1_y': P1_Y, 'p1_z': P1_Z,
            'p2_x': P2_X, 'p2_y': P2_Y, 'p2_z': P2_Z
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    assert elem.coordinate1.x == P1_X
    assert elem.coordinate1.y == P1_Y
    assert elem.coordinate1.z == P1_Z
    assert elem.coordinate2.x == P2_X
    assert elem.coordinate2.y == P2_Y
    assert elem.coordinate2.z == P2_Z
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert math.isclose(elem.distance, EXPECTED_DISTANCE)


def test_nominal_distance():
    """Test custom nominal distance element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Distance"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_distance',
        name=name,
        values={
            'p1_x': P1_X, 'p1_y': P1_Y, 'p1_z': P1_Z,
            'p2_x': P2_X, 'p2_y': P2_Y, 'p2_z': P2_Z
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.nominal_elements[name]
    assert elem.coordinate1.x == P1_X
    assert elem.coordinate1.y == P1_Y
    assert elem.coordinate1.z == P1_Z
    assert elem.coordinate2.x == P2_X
    assert elem.coordinate2.y == P2_Y
    assert elem.coordinate2.z == P2_Z
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert math.isclose(elem.distance, EXPECTED_DISTANCE)
