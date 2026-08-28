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


def _point_coordinates(point):
    if hasattr(point, 'x'):
        return point.x, point.y, point.z
    return point[0], point[1], point[2]


def _point_is_on_circle(point, center_x, radius, z_pos):
    point_x, point_y, point_z = _point_coordinates(point)
    return (
        math.isclose(
            math.hypot(point_x - center_x, point_y),
            radius,
            rel_tol=1e-6,
            abs_tol=1e-6
        )
        and math.isclose(point_z, z_pos, abs_tol=1e-6)
    )


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

    # Test objective: validate the generated defect contours. With no X-Ray
    # license, this token contains a status message instead of contour data.
    if elem.defects_points == 'Missing license (Advanced X-Ray Inspection required)':
        assert False, (
            'Meaningful VolumeDefects2d testing requires the '
            'Advanced X-Ray Inspection license.'
        )

    # defects_points contains all contour vertices as NumPy arrays, grouped
    # by defect.
    defect_points = elem.defects_points
    assert not isinstance(defect_points, str), (
        f'Unexpected defects_points status: {defect_points!r}'
    )

    assert len(defect_points) > 0, 'defects_points is empty'
    first_defect_point = defect_points[0]

    if hasattr(first_defect_point, 'x'):
        defect_contours = [defect_points]
    else:
        defect_contours = defect_points

    assert len(defect_contours) == N_DEFECTS
    assert sum(len(contour) for contour in defect_contours) == TOTAL_POINTS

    # All contour points lie in the same Z plane at Z_POS.
    # Circle centres are spaced XY_SPACING apart along X, centered on the origin.
    x_start = -0.5 * (N_DEFECTS - 1) * XY_SPACING

    centers = [
        x_start + i * XY_SPACING
        for i in range(N_DEFECTS)
    ]

    unmatched_centers = centers.copy()
    for contour in defect_contours:
        assert len(contour) == N_POINTS

        contour_center = next(
            (
                center_x
                for center_x in unmatched_centers
                if all(
                    _point_is_on_circle(point, center_x, DEFECT_RADIUS, Z_POS)
                    for point in contour
                )
            ),
            None
        )
        assert contour_center is not None, 'Invalid defects_points contour geometry'
        unmatched_centers.remove(contour_center)

    assert not unmatched_centers
