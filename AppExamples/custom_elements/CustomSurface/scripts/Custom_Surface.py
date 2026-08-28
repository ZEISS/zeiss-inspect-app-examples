"""
Custom nominal/actual Surface Element Example

Carl Zeiss GOM Metrology GmbH, 2026

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import gom.api.extensions.nominals

from gom import apicontribution

# Fixed triangle indices defining a cuboid from 8 vertices:
# two triangles per face, 6 faces = 12 triangles total
CUBOID_TRIANGLES = [
    # front (x+)
    (0, 1, 2), (0, 2, 3),
    # right (y+)
    (1, 5, 6), (1, 6, 2),
    # top (z+)
    (3, 2, 6), (3, 6, 7),
    # bottom (z-)
    (0, 1, 5), (0, 5, 4),
    # back (x-)
    (4, 5, 6), (4, 6, 7),
    # left (y-)
    (0, 4, 7), (0, 7, 3),
]


def _compute_surface(values):
    """Compute cuboid surface from 8 corner vertex values."""
    # -------------------------------------------------------------------------
    vertices = []
    for i in range(8):
        vertices.append((
            float(values[f'v{i}_x']),
            float(values[f'v{i}_y']),
            float(values[f'v{i}_z'])
        ))
    return vertices, CUBOID_TRIANGLES, len(vertices)
    # -------------------------------------------------------------------------


@apicontribution
class ActualSurface(gom.api.extensions.actuals.Surface):
    """
    Custom actual surface element.

    Features:
    - Creates a cuboid surface mesh from 8 user-defined corner vertices
    - Triangle connectivity is fixed (two triangles per face, 12 total)
    - Stores num_vertices as a custom element data token
    """

    def __init__(self):
        """Register the custom actual surface contribution."""
        super().__init__(id='examples.custom_actual_surface', description='Custom Actual Surface')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Surface.gdlg')

    def compute(self, _context, values):
        """Compute the actual surface element."""
        # -------------------------------------------------------------------------
        vertices, triangles, num_vertices = _compute_surface(values)
        return {
            "vertices": vertices,
            "triangles": triangles,
            "data": {"num_vertices": num_vertices}
        }
        # -------------------------------------------------------------------------


@apicontribution
class NominalSurface(gom.api.extensions.nominals.Surface):
    """
    Custom nominal surface element.

    Features:
    - Creates a cuboid surface mesh from 8 user-defined corner vertices
    - Triangle connectivity is fixed (two triangles per face, 12 total)
    - Stores num_vertices as a custom element data token
    """

    def __init__(self):
        """Register the custom nominal surface contribution."""
        super().__init__(id='examples.custom_nominal_surface', description='Custom Nominal Surface')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Surface.gdlg')

    def compute(self, _context, values):
        """Compute the nominal surface element."""
        # -------------------------------------------------------------------------
        vertices, triangles, num_vertices = _compute_surface(values)
        return {
            "vertices": vertices,
            "triangles": triangles,
            "data": {"num_vertices": num_vertices}
        }
        # -------------------------------------------------------------------------


gom.run_api()
