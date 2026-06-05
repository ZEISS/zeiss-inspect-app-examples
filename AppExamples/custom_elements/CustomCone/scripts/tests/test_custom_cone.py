"""
Test for custom cone element
"""

import gom
import gom.api.services

SERVICE_ENDPOINT = 'gom.api.examples.custom_cone'
SERVICE_TIMEOUT = 10000

P1_X = 0.0
P1_Y = 0.0
P1_Z = 0.0
RADIUS1 = 10.0
P2_X = 0.0
P2_Y = 0.0
P2_Z = 100.0
RADIUS2 = 20.0


def test_actual_cone():
    """Test custom actual cone element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual Cone"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_cone',
        name=name,
        values={
            'p1_x': P1_X, 'p1_y': P1_Y, 'p1_z': P1_Z, 'radius1': RADIUS1,
            'p2_x': P2_X, 'p2_y': P2_Y, 'p2_z': P2_Z, 'radius2': RADIUS2
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.radius1 == RADIUS1
    assert elem.radius2 == RADIUS2


def test_nominal_cone():
    """Test custom nominal cone element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Nominal Cone"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_cone',
        name=name,
        values={
            'p1_x': P1_X, 'p1_y': P1_Y, 'p1_z': P1_Z, 'radius1': RADIUS1,
            'p2_x': P2_X, 'p2_y': P2_Y, 'p2_z': P2_Z, 'radius2': RADIUS2
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.nominal_elements[name]
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.radius1 == RADIUS1
    assert elem.radius2 == RADIUS2
