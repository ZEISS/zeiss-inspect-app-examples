"""
Custom nominal/actual Cone Element Example

Carl Zeiss GOM Metrology GmbH, 2026

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import gom.api.extensions.nominals

from gom import apicontribution


@apicontribution
class ActualCone(gom.api.extensions.actuals.Cone):
    """
    Custom actual cone element.

    Features:
    - Creates a cone defined by two circles (each given by a point and a radius)
    - Stores the two radii as custom element data tokens (radius1, radius2)
    """

    def __init__(self):
        """Register the custom actual cone contribution."""
        super().__init__(id='examples.custom_actual_cone', description='Custom Actual Cone')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Cone.gdlg')

    def compute_stage(self, _context, values):
        """Compute the actual cone element."""
        point1 = (float(values['p1_x']), float(values['p1_y']), float(values['p1_z']))
        radius1 = float(values['radius1'])
        point2 = (float(values['p2_x']), float(values['p2_y']), float(values['p2_z']))
        radius2 = float(values['radius2'])
        return {
            "point1": point1,
            "radius1": radius1,
            "point2": point2,
            "radius2": radius2,
            "data": {"radius1": radius1, "radius2": radius2}
        }


@apicontribution
class NominalCone(gom.api.extensions.nominals.Cone):
    """
    Custom nominal cone element.

    Features:
    - Creates a cone defined by two circles (each given by a point and a radius)
    - Stores the two radii as custom element data tokens (radius1, radius2)
    """

    def __init__(self):
        """Register the custom nominal cone contribution."""
        super().__init__(id='examples.custom_nominal_cone', description='Custom Nominal Cone')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Cone.gdlg')

    def compute_stage(self, _context, values):
        """Compute the nominal cone element."""
        point1 = (float(values['p1_x']), float(values['p1_y']), float(values['p1_z']))
        radius1 = float(values['radius1'])
        point2 = (float(values['p2_x']), float(values['p2_y']), float(values['p2_z']))
        radius2 = float(values['radius2'])
        return {
            "point1": point1,
            "radius1": radius1,
            "point2": point2,
            "radius2": radius2,
            "data": {"radius1": radius1, "radius2": radius2}
        }


gom.run_api()
