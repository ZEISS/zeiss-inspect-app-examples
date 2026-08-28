"""
Custom nominal/actual Point Cloud Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import gom.api.extensions.nominals
import math
import numpy as np

from gom import apicontribution


def _compute_point_cloud(values):
    """
    Compute toroid (donut) point cloud from dialog values.

    Uses the parametric surface formula:
                / (R + r*cos(v*pi))*cos(u*pi) \
    P(u, v) =  |  (R + r*cos(v*pi))*sin(u*pi)  |
                \  r*sin(v*pi)                /
    with u in [u_min...u_max], v in [v_min...v_max]
    """
    # -------------------------------------------------------------------------
    R = float(values['R'])
    r = float(values['r'])
    u_min = float(values['u_min'])
    u_max = float(values['u_max'])
    u_steps = int(values['u_steps'])
    v_min = float(values['v_min'])
    v_max = float(values['v_max'])
    v_steps = int(values['v_steps'])

    points = []
    normals = []
    for u in np.arange(u_min, u_max, (u_max - u_min) / u_steps):
        for v in np.arange(v_min, v_max, (v_max - v_min) / v_steps):
            cos_u = math.cos(u * math.pi)
            sin_u = math.sin(u * math.pi)
            cos_v = math.cos(v * math.pi)
            sin_v = math.sin(v * math.pi)
            points.append((
                (R + r * cos_v) * cos_u,
                (R + r * cos_v) * sin_u,
                r * sin_v
            ))
            # Outward unit normal of the toroid surface
            normals.append((cos_v * cos_u, cos_v * sin_u, sin_v))

    num_points = len(points)
    u_range = u_max - u_min
    return points, normals, num_points, u_range
    # -------------------------------------------------------------------------


@apicontribution
class ActualPointCloud(gom.api.extensions.actuals.PointCloud):
    """
    Custom actual point cloud element.

    Features:
    - Creates a toroid (donut) point cloud from a parametric surface formula
    - Parameters: major radius R, minor radius r, u/v ranges and step counts
    - Stores num_points and u_range as custom element data tokens
    """

    def __init__(self):
        """Register the custom actual point cloud contribution."""
        super().__init__(id='examples.custom_actual_point_cloud', description='Custom Actual Point Cloud')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_PointCloud.gdlg')

    def compute(self, context, values):
        """Compute the actual point cloud element."""
        # -------------------------------------------------------------------------
        points, normals, num_points, u_range = _compute_point_cloud(values)
        return {
            "points": points,
            "normals": normals,
            "data": {"num_points": num_points, "u_range": u_range}
        }
        # -------------------------------------------------------------------------


@apicontribution
class NominalPointCloud(gom.api.extensions.nominals.PointCloud):
    """
    Custom nominal point cloud element.

    Features:
    - Creates a toroid (donut) point cloud from a parametric surface formula
    - Parameters: major radius R, minor radius r, u/v ranges and step counts
    - Stores num_points and u_range as custom element data tokens
    """

    def __init__(self):
        """Register the custom nominal point cloud contribution."""
        super().__init__(id='examples.custom_nominal_point_cloud', description='Custom Nominal Point Cloud')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_PointCloud.gdlg')

    def compute(self, context, values):
        """Compute the nominal point cloud element."""
        # -------------------------------------------------------------------------
        points, normals, num_points, u_range = _compute_point_cloud(values)
        return {
            "points": points,
            "normals": normals,
            "data": {"num_points": num_points, "u_range": u_range}
        }
        # -------------------------------------------------------------------------


gom.run_api()
