"""
Custom actual VolumeDefects2d Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples

NOTE: This example requires ZEISS INSPECT X-Ray.

Demonstrates the gom.api.extensions.actuals.VolumeDefects2d compute format:
each curve is a planar circular contour representing one pore/void detected on
a CT scan slice. Several such defect circles are placed along the Z-axis.
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import math

from gom import apicontribution


def _compute_defect_contours(values):
    """
    Build coplanar circular defect contours on a single CT scan slice.

    All circles lie in the XY-plane at z = z_pos. The n_defects circle
    centres are spaced xy_spacing apart along the X-axis, centred on the
    origin. Each circle is discretised into n_points 3D coordinates.

    All curves must be coplanar — this is a hard requirement of the
    VolumeDefects2d element type.

    :param values: dict with keys n_defects, defect_radius, z_pos,
                   xy_spacing, n_points
    :returns: list of contours, where each contour is a list of (x, y, z) tuples
    """
    n_defects = int(values['n_defects'])
    defect_radius = float(values['defect_radius'])
    z_pos = float(values['z_pos'])
    xy_spacing = float(values['xy_spacing'])
    n_points = int(values['n_points'])

    # Centre the row of defects symmetrically around the origin
    x_start = -0.5 * (n_defects - 1) * xy_spacing

    curves = []
    # -------------------------------------------------------------------------
    for i in range(n_defects):
        cx = x_start + i * xy_spacing
        contour = []
        for j in range(n_points):
            angle = 2.0 * math.pi * j / n_points
            x = cx + defect_radius * math.cos(angle)
            y = defect_radius * math.sin(angle)
            contour.append((x, y, z_pos))
        curves.append(contour)
    # -------------------------------------------------------------------------
    return curves


@apicontribution
class ActualVolumeDefects2d(gom.api.extensions.actuals.VolumeDefects2d):
    """
    Custom actual 2D volume defects element.

    Features:
    - Creates n_defects circular contours in the XY-plane, all at the same Z slice
    - Contour points: (defect_radius * cos(2π·j/n_points), defect_radius * sin(2π·j/n_points), z)
    - Circle centres are spaced along X by xy_spacing and centered around the origin
    - Stores num_defects and total_points as custom element data tokens
    """

    def __init__(self):
        """Register the custom actual 2D volume defects contribution."""
        super().__init__(
            id='examples.custom_actual_volume_defects_2d',
            description='Custom Actual VolumeDefects2d'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_VolumeDefects2d.gdlg')

    def compute_stage(self, _context, values):
        """Compute the actual 2D volume defects element."""
        # -------------------------------------------------------------------------
        curves = _compute_defect_contours(values)
        n_defects = int(values['n_defects'])
        n_points = int(values['n_points'])
        return {
            'curves': curves,
            'data': {
                'num_defects': n_defects,
                'total_points': n_defects * n_points
            }
        }
        # -------------------------------------------------------------------------


gom.run_api()
