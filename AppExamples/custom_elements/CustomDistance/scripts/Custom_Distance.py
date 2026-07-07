"""
Custom nominal/actual Distance Element Example

Carl Zeiss GOM Metrology GmbH, 2026

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import math

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import gom.api.extensions.nominals

from gom import apicontribution


@apicontribution
class ActualDistance(gom.api.extensions.actuals.Distance):
    """
    Custom actual distance element.

    Features:
    - Creates a distance element from two user-defined points
    - Stores the Euclidean distance between the points as a custom element data token (distance)
    """

    def __init__(self):
        """Register the custom actual distance contribution."""
        super().__init__(
            id='examples.custom_actual_distance',
            description='Custom Actual Distance'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Distance.gdlg')

    def compute(self, _context, values):
        """Compute the actual distance element."""
        point1 = (float(values['p1_x']), float(values['p1_y']), float(values['p1_z']))
        point2 = (float(values['p2_x']), float(values['p2_y']), float(values['p2_z']))
        dx = float(values['p2_x']) - float(values['p1_x'])
        dy = float(values['p2_y']) - float(values['p1_y'])
        dz = float(values['p2_z']) - float(values['p1_z'])
        distance = math.sqrt(dx * dx + dy * dy + dz * dz)
        return {
            "point1": point1,
            "point2": point2,
            "data": {"distance": distance}
        }


@apicontribution
class NominalDistance(gom.api.extensions.nominals.Distance):
    """
    Custom nominal distance element.

    Features:
    - Creates a distance element from two user-defined points
    - Stores the Euclidean distance between the points as a custom element data token (distance)
    """

    def __init__(self):
        """Register the custom nominal distance contribution."""
        super().__init__(
            id='examples.custom_nominal_distance',
            description='Custom Nominal Distance'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Distance.gdlg')

    def compute(self, _context, values):
        """Compute the nominal distance element."""
        point1 = (float(values['p1_x']), float(values['p1_y']), float(values['p1_z']))
        point2 = (float(values['p2_x']), float(values['p2_y']), float(values['p2_z']))
        dx = float(values['p2_x']) - float(values['p1_x'])
        dy = float(values['p2_y']) - float(values['p1_y'])
        dz = float(values['p2_z']) - float(values['p1_z'])
        distance = math.sqrt(dx * dx + dy * dy + dz * dz)
        return {
            "point1": point1,
            "point2": point2,
            "data": {"distance": distance}
        }


gom.run_api()
