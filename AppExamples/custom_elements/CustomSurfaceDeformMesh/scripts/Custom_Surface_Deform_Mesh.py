"""
Custom actual surface element created by deforming an existing mesh.

Carl Zeiss GOM Metrology GmbH, 2026

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import numpy as np
import trimesh

from gom import apicontribution


def _mesh_result(element, stage, deformation):
    """Apply trimesh noise to one stage of the selected element."""
    vertices = np.array(element.data.coordinate)[stage]
    triangles = np.array(element.data.triangle)[stage]
    mesh = trimesh.Trimesh(vertices, triangles)
    deformed = trimesh.permutate.noise(mesh, deformation)
    return {
        'vertices': deformed.vertices,
        'triangles': np.array(deformed.faces, dtype=np.int32)
    }


@apicontribution
class ActualSurfaceDeformMesh(gom.api.extensions.actuals.Surface):
    """Custom actual surface generated from a deformed mesh."""

    def __init__(self):
        super().__init__(
            id='examples.custom_actual_surface_deform_mesh',
            description='Custom Actual Surface Deform Mesh'
        )

    def element_filter(self, element):
        """Accept mesh and CAD body elements as deformation sources."""
        try:
            return element.type in ['mesh', 'cad_body']
        except (AttributeError, TypeError):
            return False

    def dialog(self, context, args):
        """Show the dialog and attach the source-element filter."""
        dialog = gom.api.dialog.create(context, '/Custom_Surface_Deform_Mesh.gdlg')
        dialog.selected_element.filter = self.element_filter

        def update_element_name():
            selected_element = dialog.selected_element.value
            if selected_element is not None:
                dialog.name.basename = f'{selected_element.name}.deformed'

        def dialog_handler(widget):
            if widget == dialog.selected_element or str(widget) in ('initialize', 'system'):
                update_element_name()

        dialog.handler = dialog_handler
        self.initialize_dialog(context, dialog, args)
        update_element_name()
        result = gom.api.dialog.show(context, dialog)
        params = self.apply_dialog(dialog, result)
        params['selected_element'] = result['selected_element']
        params['deformation_value'] = result['deformation_value']
        return params

    def compute(self, context, values):
        """Compute the deformed surface for the current stage."""
        return _mesh_result(
            values['selected_element'],
            context.stage,
            float(values['deformation_value'])
        )


gom.run_api()