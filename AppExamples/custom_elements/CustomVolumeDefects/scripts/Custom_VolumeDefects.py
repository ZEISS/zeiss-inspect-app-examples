"""
Custom actual VolumeDefects Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples

NOTE: This example requires ZEISS INSPECT X-Ray.

Mirrors the functionality of the ScriptedActualVolumeDefects example:
a tetrahedral volume defect defined by four user-supplied vertices.
The triangles connecting the vertices are fixed (counter-clockwise order).
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import numpy as np

from gom import apicontribution


def _create_defects(values):
    """
    Build a tetrahedral volume defect mesh from four vertices.

    The four vertices define a tetrahedron with four triangular faces.
    Triangle vertices must be specified in counter-clockwise order so that
    the surface normals point outward (inward-facing normals make the surface
    invisible in the ZEISS INSPECT viewer).

    :param values: dict containing v0_x/y/z … v3_x/y/z (LENGTH)
    :returns: dict with 'vertices' and 'triangles' numpy arrays
    """
    v0 = (values['v0_x'], values['v0_y'], values['v0_z'])
    v1 = (values['v1_x'], values['v1_y'], values['v1_z'])
    v2 = (values['v2_x'], values['v2_y'], values['v2_z'])
    v3 = (values['v3_x'], values['v3_y'], values['v3_z'])

    triangles = np.array([(0, 1, 2), (1, 0, 3), (0, 2, 3), (2, 1, 3)], dtype=np.int32)

    # -------------------------------------------------------------------------
    return {
        'vertices': [np.array([v0, v1, v2, v3], dtype=np.float64)],
        # Triangles are indices into the vertex array.
        # Vertices must be in counter-clockwise order; otherwise the surface
        # is inverted (invisible).
        'triangles': [triangles],
        'data': {
            'num_vertices': 4,
            'num_triangles': len(triangles)
        }
    }
    # -------------------------------------------------------------------------


@apicontribution
class ActualVolumeDefects(gom.api.extensions.actuals.VolumeDefects):
    """
    Custom actual volume defects element.

    Features:
    - Tetrahedral 3D volume defect defined by four user-supplied vertices
    - Fixed triangulation: four counter-clockwise triangular faces
    """

    def __init__(self):
        """Register the custom actual volume defects contribution."""
        super().__init__(
            id='examples.custom_actual_volume_defects',
            description='Custom Actual Volume Defects'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_VolumeDefects.gdlg')

    def compute(self, context, values):
        """Compute the actual volume defects element."""
        return _create_defects(values)


gom.run_api()
