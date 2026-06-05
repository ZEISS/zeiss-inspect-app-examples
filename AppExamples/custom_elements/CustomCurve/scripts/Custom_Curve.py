"""
Custom nominal/actual Curve Element Example

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


def _compute_curve_points(values):
    """
    Compute curve points using the parametric formula:
    P(t) = ( x0 + (j * t + r) * cos(t), y0 + (j * t + r) * sin(t), z0 + k * t )
    with NUM_STEPS evenly spaced steps in [t_min, t_max).
    """
    x0 = float(values['x0'])
    y0 = float(values['y0'])
    z0 = float(values['z0'])
    r = float(values['radius'])
    j = float(values['j'])
    k = float(values['k'])
    t_min = float(values['t_min'])
    t_max = float(values['t_max'])
    step = (t_max - t_min) / NUM_STEPS
    points = []
    for i in range(NUM_STEPS):
        t = t_min + i * step
        points.append((
            x0 + (j * t + r) * math.cos(t),
            y0 + (j * t + r) * math.sin(t),
            z0 + k * t
        ))
    return points


@apicontribution
class ActualCurve(gom.api.extensions.actuals.Curve):
    """
    Custom actual curve element.

    Features:
    - Creates a curve from the parametric formula P(t) = ( x0 + (j*t+r)*cos(t), y0 + (j*t+r)*sin(t), z0 + k*t )
    - Stores the point count as a custom element data token (num_points)
    """

    def __init__(self):
        """Register the custom actual curve contribution."""
        super().__init__(id='examples.custom_actual_curve', description='Custom Actual Curve')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Curve.gdlg')

    def compute_stage(self, _context, values):
        """Compute the actual curve element."""
        # -------------------------------------------------------------------------
        points = _compute_curve_points(values)
        t_range = float(values['t_max']) - float(values['t_min'])
        return {
            "curves": [{"points": points}],
            "data": {"num_points": len(points), "t_range": t_range}
        }
        # -------------------------------------------------------------------------


@apicontribution
class NominalCurve(gom.api.extensions.nominals.Curve):
    """
    Custom nominal curve element.

    Features:
    - Creates a curve from the parametric formula P(t) = ( x0 + (j*t+r)*cos(t), y0 + (j*t+r)*sin(t), z0 + k*t )
    - Stores the point count as a custom element data token (num_points)
    """

    def __init__(self):
        """Register the custom nominal curve contribution."""
        super().__init__(id='examples.custom_nominal_curve', description='Custom Nominal Curve')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Curve.gdlg')

    def compute_stage(self, _context, values):
        """Compute the nominal curve element."""
        # -------------------------------------------------------------------------
        points = _compute_curve_points(values)
        t_range = float(values['t_max']) - float(values['t_min'])
        return {
            "curves": [{"points": points}],
            "data": {"num_points": len(points), "t_range": t_range}
        }
        # -------------------------------------------------------------------------


gom.run_api()
