"""
Custom nominal/actual Circle Element Example

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
class ActualCircle(gom.api.extensions.actuals.Circle):
    """
    Custom actual circle element.

    Features:
    - Creates a circle from user-defined center, direction, and radius
    - Stores the center coordinates as custom element data tokens (center_x, center_y, center_z)
    """

    def __init__(self):
        """Register the custom actual circle contribution."""
        super().__init__(id='examples.custom_actual_circle', description='Custom Actual Circle')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Circle.gdlg')

    def compute_stage(self, _context, values):
        """Compute the actual circle element."""
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
class NominalCircle(gom.api.extensions.nominals.Circle):
    """
    Custom nominal circle element.

    Features:
    - Creates a circle from user-defined center, direction, and radius
    - Stores the center coordinates as custom element data tokens (center_x, center_y, center_z)
    """

    def __init__(self):
        """Register the custom nominal circle contribution."""
        super().__init__(
            id='examples.custom_nominal_circle',
            description='Custom Nominal Circle'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Circle.gdlg')

    def compute_stage(self, _context, values):
        """Compute the nominal circle element."""
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
