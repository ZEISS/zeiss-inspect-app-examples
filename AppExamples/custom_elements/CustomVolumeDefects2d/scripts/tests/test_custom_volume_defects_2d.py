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
    # Circle centres are spaced XY_SPACING apart along X, centered on the origin.
    x_start = -0.5 * (N_DEFECTS - 1) * XY_SPACING

    # The coordinate token is a flat list with one representative Vec3d per
    # defect; it does not expose the individual contour vertices. The custom
    # total_points token above verifies the full contour vertex count.
    coords = list(elem.coordinate)

    assert len(coords) == N_DEFECTS

    centers = [
        x_start + i * XY_SPACING
        for i in range(N_DEFECTS)
    ]

    unmatched_centers = centers.copy()
    for point in coords:
        assert math.isclose(point.z, Z_POS, abs_tol=1e-6)

        matching_center = next(
            (
                center_x
                for center_x in unmatched_centers
                if math.isclose(
                    math.hypot(point.x - center_x, point.y),
                    DEFECT_RADIUS,
                    rel_tol=1e-6,
                    abs_tol=1e-6
                )
            ),
            None
        )
        assert matching_center is not None, f"Point is not on a defect circle: {point}"
        unmatched_centers.remove(matching_center)

    assert not unmatched_centers
