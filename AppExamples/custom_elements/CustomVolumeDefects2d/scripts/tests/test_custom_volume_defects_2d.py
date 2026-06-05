"""
Test for custom VolumeDefects2d element
"""

import math
import gom
import gom.api.services

SERVICE_ENDPOINT = 'gom.api.examples.custom_volume_defects_2d'
SERVICE_TIMEOUT = 10000

N_DEFECTS = 3
DEFECT_RADIUS = 5.0
Z_POS = 0.0
XY_SPACING = 15.0
N_POINTS = 36
TOTAL_POINTS = N_DEFECTS * N_POINTS


def test_actual_volume_defects_2d():
    """Test custom actual 2D volume defects element."""
    gom.script.sys.close_project()
    gom.script.sys.create_project()

    service = gom.api.services.get_service(SERVICE_ENDPOINT)
    if not service.get_status() == 'RUNNING':
        if not service.start_and_wait(timeout=SERVICE_TIMEOUT):
            assert False, f"Failed to start service {SERVICE_ENDPOINT}"

    name = "Actual VolumeDefects2d"
    gom.script.customelements.create_actual(
        contribution='examples.custom_actual_volume_defects_2d',
        name=name,
        values={
            'n_defects': N_DEFECTS,
            'defect_radius': DEFECT_RADIUS,
            'z_pos': Z_POS,
            'xy_spacing': XY_SPACING,
            'n_points': N_POINTS
        }
    )

    #
    # TEST
    #
    elem = gom.app.project.actual_elements[name]
    # Check custom element data tokens
    assert elem.num_defects == N_DEFECTS
    assert elem.total_points == TOTAL_POINTS

    # All defects lie in the same Z plane at Z_POS.
    # Circle centres are spaced XY_SPACING apart along X, centred on the origin.
    # x_start = -0.5 * (N_DEFECTS - 1) * XY_SPACING
    x_start = -0.5 * (N_DEFECTS - 1) * XY_SPACING

    coords = list(elem.data.coordinate)

    # First point of the first contour: (x_start + DEFECT_RADIUS, 0, Z_POS)
    first_point = coords[0]
    assert math.isclose(first_point[0], x_start + DEFECT_RADIUS, rel_tol=1e-6)
    assert math.isclose(first_point[1], 0.0, abs_tol=1e-6)
    assert math.isclose(first_point[2], Z_POS, abs_tol=1e-6)

    # All points must share the same Z (coplanar requirement)
    for pt in coords:
        assert math.isclose(pt[2], Z_POS, abs_tol=1e-6), f"Non-coplanar point: z={pt[2]}"
