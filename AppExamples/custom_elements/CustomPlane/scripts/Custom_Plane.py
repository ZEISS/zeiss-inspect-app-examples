"""
Custom nominal/actual Plane Element Example

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
class ActualPlane(gom.api.extensions.actuals.Plane):
    """
    Custom actual plane element.

    Features:
    - Creates a plane from a user-defined normal vector and a point on the plane
    - Stores the normal vector components as custom element data tokens
      (normal_x, normal_y, normal_z)
    """

    def __init__(self):
        """Register the custom actual plane contribution."""
        super().__init__(id='examples.custom_actual_plane', description='Custom Actual Plane')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Plane.gdlg')

    def compute_stage(self, _context, values):
        """Compute the actual plane element."""
        nx, ny, nz = float(values['normal_x']), float(values['normal_y']), float(values['normal_z'])
        normal = (nx, ny, nz)
        point = (
            float(values['point_x']),
            float(values['point_y']),
            float(values['point_z'])
        )
        return {
            "normal": normal,
            "point": point,
            "data": {"normal_x": nx, "normal_y": ny, "normal_z": nz}
        }


@apicontribution
class NominalPlane(gom.api.extensions.nominals.Plane):
    """
    Custom nominal plane element.

    Features:
    - Creates a plane from a user-defined normal vector and a point on the plane
    - Stores the normal vector components as custom element data tokens
      (normal_x, normal_y, normal_z)
    """

    def __init__(self):
        """Register the custom nominal plane contribution."""
        super().__init__(id='examples.custom_nominal_plane', description='Custom Nominal Plane')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Plane.gdlg')

    def compute_stage(self, _context, values):
        """Compute the nominal plane element."""
        nx, ny, nz = float(values['normal_x']), float(values['normal_y']), float(values['normal_z'])
        normal = (nx, ny, nz)
        point = (
            float(values['point_x']),
            float(values['point_y']),
            float(values['point_z'])
        )
        return {
            "normal": normal,
            "point": point,
            "data": {"normal_x": nx, "normal_y": ny, "normal_z": nz}
        }


gom.run_api()
