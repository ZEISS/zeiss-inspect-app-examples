"""
Custom nominal/actual Surface Curve Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import gom.api.extensions.nominals
import math

from gom import apicontribution

NUM_STEPS = 1000


def _compute_surface_curve(values):
    """
    Compute a sphere section curve at fixed elevation angle theta.

    P(phi) = ( r * cos(theta) * cos(phi),
               r * cos(theta) * sin(phi),
               r * sin(theta) )

    Normals equal the point coordinates (outward radial, not normalized).
    """
    r = float(values['r'])
    theta = float(values['theta'])
    phi_min = float(values['phi_min'])
    phi_max = float(values['phi_max'])

    r_cos_theta = r * math.cos(theta)
    z = r * math.sin(theta)
    step = (phi_max - phi_min) / NUM_STEPS

    points = []
    normals = []
    for i in range(NUM_STEPS):
        phi = phi_min + i * step
        p = (r_cos_theta * math.cos(phi), r_cos_theta * math.sin(phi), z)
        points.append(p)
        normals.append(p)  # normals = same as points (outward radial, not normalized)

    phi_range = phi_max - phi_min
    return points, normals, phi_range


@apicontribution
class ActualSurfaceCurve(gom.api.extensions.actuals.SurfaceCurve):
    """
    Custom actual surface curve element.

    Features:
    - Creates a sphere section curve at a fixed elevation angle theta
    - Azimuth angle phi varies from phi_min to phi_max in NUM_STEPS steps
    - Normals equal the point coordinates (outward radial, not normalized)
    - Stores num_points and phi_range as custom element data tokens
    """

    def __init__(self):
        """Register the custom actual surface curve contribution."""
        super().__init__(id='examples.custom_actual_surface_curve', description='Custom Actual Surface Curve')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_SurfaceCurve.gdlg')

    def compute_stage(self, _context, values):
        """Compute the actual surface curve element."""
        # -------------------------------------------------------------------------
        points, normals, phi_range = _compute_surface_curve(values)
        return {
            "curves": [{"points": points, "normals": normals}],
            "data": {"num_points": len(points), "phi_range": phi_range}
        }
        # -------------------------------------------------------------------------


@apicontribution
class NominalSurfaceCurve(gom.api.extensions.nominals.SurfaceCurve):
    """
    Custom nominal surface curve element.

    Features:
    - Creates a sphere section curve at a fixed elevation angle theta
    - Azimuth angle phi varies from phi_min to phi_max in NUM_STEPS steps
    - Normals equal the point coordinates (outward radial, not normalized)
    - Stores num_points and phi_range as custom element data tokens
    """

    def __init__(self):
        """Register the custom nominal surface curve contribution."""
        super().__init__(id='examples.custom_nominal_surface_curve', description='Custom Nominal Surface Curve')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_SurfaceCurve.gdlg')

    def compute_stage(self, _context, values):
        """Compute the nominal surface curve element."""
        # -------------------------------------------------------------------------
        points, normals, phi_range = _compute_surface_curve(values)
        return {
            "curves": [{"points": points, "normals": normals}],
            "data": {"num_points": len(points), "phi_range": phi_range}
        }
        # -------------------------------------------------------------------------


gom.run_api()
