"""
Custom nominal/actual Cylinder Element Example

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
class ActualCylinder(gom.api.extensions.actuals.Cylinder):
    """
    Custom actual cylinder element.

    Features:
        - Creates a cylinder from user-defined center point, direction, and radius
        - Stores the center point coordinates as custom element data tokens (center_x, center_y, center_z)
    """

    def __init__(self):
        """Register the custom actual cylinder contribution."""
        super().__init__(
            id='examples.custom_actual_cylinder',
            description='Custom Actual Cylinder'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Cylinder.gdlg')

    def compute(self, _context, values):
        """Compute the actual cylinder element."""
        center = (
            float(values['center_x']),
            float(values['center_y']),
            float(values['center_z'])
        )
        direction = (
            float(values['dir_x']),
            float(values['dir_y']),
            float(values['dir_z'])
        )
        radius = float(values['radius'])
        return {
            "center": center,
            "direction": direction,
            "radius": radius,
            "data": {
                "center_x": float(values['center_x']),
                "center_y": float(values['center_y']),
                "center_z": float(values['center_z'])
            }
        }


@apicontribution
class NominalCylinder(gom.api.extensions.nominals.Cylinder):
    """
    Custom nominal cylinder element.

    Features:
        - Creates a cylinder from user-defined center point, direction, and radius
        - Stores the center point coordinates as custom element data tokens (center_x, center_y, center_z)
                - Uses the same 'center' geometry key as the actual cylinder API
    """

    def __init__(self):
        """Register the custom nominal cylinder contribution."""
        super().__init__(
            id='examples.custom_nominal_cylinder',
            description='Custom Nominal Cylinder'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Cylinder.gdlg')

    def compute(self, _context, values):
        """
        Compute the nominal cylinder element.
        """
        center = (
            float(values['center_x']),
            float(values['center_y']),
            float(values['center_z'])
        )
        direction = (
            float(values['dir_x']),
            float(values['dir_y']),
            float(values['dir_z'])
        )
        radius = float(values['radius'])
        return {
            "center": center,
            "direction": direction,
            "radius": radius,
            "data": {
                "center_x": float(values['center_x']),
                "center_y": float(values['center_y']),
                "center_z": float(values['center_z'])
            }
        }


gom.run_api()
