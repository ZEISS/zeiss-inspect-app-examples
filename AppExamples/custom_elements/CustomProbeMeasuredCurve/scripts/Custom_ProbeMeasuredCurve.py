"""
Custom actual Probe Measured Curve Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import math

from gom import apicontribution

NUM_POINTS = 500


def _compute_probe_measured_curve(values):
    """
    Compute a helix of probe-contact points on a cylinder surface.

    This simulates a CMM tactile probe tracing a helical groove, e.g. when
    measuring a screw thread. The probe center moves along the helix:

        P(t) = ( R*cos(2π*n*t), R*sin(2π*n*t), H*t )   t ∈ [0, 1]

    where R = cylinder radius, H = height, n = number of turns.
    Each probe-contact point carries the same uniform probe tip radius.
    """
    cylinder_radius = float(values['cylinder_radius'])
    height = float(values['height'])
    n_turns = float(values['n_turns'])
    probe_radius = float(values['probe_radius'])

    points = []
    radii = []
    for i in range(NUM_POINTS):
        t = i / (NUM_POINTS - 1)
        angle = 2.0 * math.pi * n_turns * t
        x = cylinder_radius * math.cos(angle)
        y = cylinder_radius * math.sin(angle)
        z = height * t
        points.append((x, y, z))
        radii.append(probe_radius)

    pitch = height / n_turns if n_turns != 0.0 else 0.0
    return points, radii, pitch


@apicontribution
class ActualProbeMeasuredCurve(gom.api.extensions.actuals.ProbeMeasuredCurve):
    """
    Custom actual probe measured curve element.

    Features:
    - Simulates a CMM tactile probe tracing a helical groove on a cylinder
    - Helix: P(t) = (R·cos(2π·n·t), R·sin(2π·n·t), H·t), t ∈ [0,1]
    - All probe-contact points carry the same user-defined probe tip radius
    - Stores num_points and helix_pitch as custom element data tokens
    """

    def __init__(self):
        """Register the custom actual probe measured curve contribution."""
        super().__init__(
            id='examples.custom_actual_probe_measured_curve',
            description='Custom Actual Probe Measured Curve'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_ProbeMeasuredCurve.gdlg')

    def compute(self, _context, values):
        """Compute the actual probe measured curve element."""
        # -------------------------------------------------------------------------
        points, radii, pitch = _compute_probe_measured_curve(values)
        return {
            "curves": [{"points": points, "radii": radii}],
            "data": {"num_points": len(points), "helix_pitch": pitch}
        }
        # -------------------------------------------------------------------------


gom.run_api()
