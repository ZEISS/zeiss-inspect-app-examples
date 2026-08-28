"""
Test for custom offset point element
"""

import gom
import gom.api.services

SERVICE_ENDPOINT = 'gom.api.examples.custom_point'
SERVICE_TIMEOUT = 10000

CENTER_X = 1.0
CENTER_Y = 2.0
CENTER_Z = 3.0
OFFSET_X = 10
OFFSET_Y = 20
OFFSET_Z = 30
CIRCLE_RADIUS = 20.0


def test_actual_offset_point():
    """Test custom actual offset point element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    # Create base element
    base_element_name = "Base Circle"
    gom.script.primitive.create_auto_nominal_circle(
        name=base_element_name,
        normal={'direction': gom.Vec3d(0.0, 1.0, 0.0), 'point': gom.Vec3d(0.0, 0.0, 0.0),
                'type': 'projected'},
        point={'point': gom.Vec3d(CENTER_X, CENTER_Y, CENTER_Z)},
        radius=CIRCLE_RADIUS
    )

    # Create actual offset point element
    name = "Actual Offset Point"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_point',
        name=name,
        values={
            'base': gom.app.project.nominal_elements[base_element_name],
            'offset_x': OFFSET_X, 'offset_y': OFFSET_Y, 'offset_z': OFFSET_Z
        }
    )

    #
    # TEST
    #
    gom.log.info(f"{gom.app.project.actual_elements[name]}")
    elem = gom.app.project.actual_elements[name]
    point_actual = (
        elem.center_coordinate.x,
        elem.center_coordinate.y,
        elem.center_coordinate.z
    )
    assert (CENTER_X + OFFSET_X, CENTER_Y + OFFSET_Y, CENTER_Z + OFFSET_Z) == point_actual
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.offset_x == float(OFFSET_X)
    assert elem.offset_y == float(OFFSET_Y)
    assert elem.offset_z == float(OFFSET_Z)


def test_nominal_offset_point():
    """Test custom nominal offset point element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    # Create base element
    base_element_name = "Base Circle"
    gom.script.primitive.create_auto_nominal_circle(
        name=base_element_name,
        normal={'direction': gom.Vec3d(0.0, 1.0, 0.0), 'point': gom.Vec3d(0.0, 0.0, 0.0),
                'type': 'projected'},
        point={'point': gom.Vec3d(CENTER_X, CENTER_Y, CENTER_Z)},
        radius=CIRCLE_RADIUS
    )

    # Create nominal offset point element
    name = "Nominal Offset Point"
    gom.script.customelements.create_nominal(
        contribution='examples.custom_nominal_point',
        name=name,
        values={
            'base': gom.app.project.nominal_elements[base_element_name],
            'offset_x': OFFSET_X, 'offset_y': OFFSET_Y, 'offset_z': OFFSET_Z
        }
    )

    #
    # TEST
    #
    gom.log.info(f"{gom.app.project.nominal_elements[name]}")
    elem = gom.app.project.nominal_elements[name]
    point_nominal = (
        elem.center_coordinate.x,
        elem.center_coordinate.y,
        elem.center_coordinate.z
    )
    assert (CENTER_X + OFFSET_X, CENTER_Y + OFFSET_Y, CENTER_Z + OFFSET_Z) == point_nominal
    # Check custom element data tokens (stored via 'data' key in compute result)
    assert elem.offset_x == float(OFFSET_X)
    assert elem.offset_y == float(OFFSET_Y)
    assert elem.offset_z == float(OFFSET_Z)
