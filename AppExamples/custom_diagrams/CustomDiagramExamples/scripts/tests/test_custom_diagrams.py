"""
Integration test for the custom diagram examples.

The actual custom diagram rendering has to be verified manually, but this test ensures
that the custom diagram services can be started and that the custom circle elements can be created
and have the expected properties.
"""

import gom
import gom.api.services

SERVICE_ENDPOINTS = (
    'gom.api.examples.custom_diagrams',
    'gom.api.examples.custom_diagrams_basic',
    'gom.api.examples.custom_diagrams.element_overlay',
    'gom.api.examples.custom_diagrams.point_cloud_overlay',
)
SERVICE_TIMEOUT = 10000
CIRCLE_CONTRIBUTION = 'examples.custom_diagrams.actual_circle'
CIRCLE_VALUES = (
    ("Circle 1", 10.0, 20.0, 30.0, 5.0),
    ("Circle 2", 40.0, 50.0, 60.0, 15.0),
    ("Circle 3", 70.0, 80.0, 90.0, 25.0),
)


def _start_services():
    """Start the custom circle and diagram services used by this test."""
    for endpoint in SERVICE_ENDPOINTS:
        service = gom.api.services.get_service(endpoint)
        if service.get_status() != 'RUNNING':
            if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
                assert False, f"Failed to start service {endpoint}"


def test_custom_diagrams_with_circles():
    """Create several circles while all custom diagram services are running."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()
    _start_services()

    for name, center_x, center_y, center_z, radius in CIRCLE_VALUES:
        gom.script.customelements.create_actual(
            contribution=CIRCLE_CONTRIBUTION,
            name=name,
            values={
                'center_x': center_x,
                'center_y': center_y,
                'center_z': center_z,
                'dir_x': 0.0,
                'dir_y': 0.0,
                'dir_z': 1.0,
                'radius': radius,
            }
        )

    for name, center_x, center_y, center_z, radius in CIRCLE_VALUES:
        element = gom.app.project.actual_elements[name]
        assert element.center_coordinate.x == center_x
        assert element.center_coordinate.y == center_y
        assert element.center_coordinate.z == center_z
        assert element.diameter / 2.0 == radius
        assert element.radius == radius
