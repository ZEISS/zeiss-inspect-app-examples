"""
CustomSurfaceInspection Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples

Mirrors the functionality of the ScriptedSurfaceCheck example but uses the
modern gom.api.extensions.inspections.Surface API instead of the legacy
scripted element approach.

The check accepts any surface-checkable actual element (e.g. the part mesh)
and computes the y-coordinate of each mesh vertex as the deviation value.
The nominal reference is zero (the XZ-plane). This demonstrates how to create
a per-vertex surface inspection from a geometric property of a mesh element.
"""

import gom
import gom.api.custom_checks_util
import gom.api.dialog
import gom.api.extensions
import gom.api.extensions.inspections
import numpy as np

from gom import apicontribution


def _compute_surface_check(values, stage):
    """
    Compute per-vertex deviation values for the surface inspection.

    For each vertex of the checked mesh, the y-coordinate is used as the
    deviation value. The nominal reference is 0.0 (distance from the XZ-plane).

    :param values: dict with key 'checked_element'
    :param stage:  current stage index (from context.stage)
    :returns: dict with 'deviation_values', 'nominal', 'target_element', 'data'
    """
    element = values['checked_element']

    # -------------------------------------------------------------------------
    # Read the 3D vertex coordinates of the mesh element for the current stage.
    # The result of element.data.coordinate is a staged array; indexing with the
    # stage retrieves only the (N, 3) vertex matrix for that stage.
    vertices = np.array(element.data.coordinate)[stage]

    # Use the y-coordinate of each vertex as the deviation value.
    # nominal = 0.0 means every vertex is expected to lie on the XZ-plane.
    deviation_values = vertices[:, 1].astype(np.float32).tolist()
    # -------------------------------------------------------------------------

    return {
        'deviation_values': deviation_values,
        'nominal': 0.0,
        'target_element': element,
        'data': {
            'checked_element_name': element.name,
            'num_points': len(deviation_values)
        }
    }


@apicontribution
class CustomSurfaceInspection(gom.api.extensions.inspections.Surface):
    """
    Custom surface inspection that measures the y-deviation across a mesh.

    Features:
    - Element selector filtered to surface-checkable actual elements
    - Per-vertex deviation: deviation_values[i] = vertex.y (distance from XZ-plane)
    - Nominal reference: 0.0 (common nominal for all vertices)
    - Custom tolerance dialog using the built-in tolerance widget
    - Data tokens: checked_element_name, num_points
    """

    def __init__(self):
        """Register the custom surface inspection contribution."""
        super().__init__(
            id='examples.custom_surface_inspection',
            description='Custom Surface Inspection',
            dimension='LENGTH',
            abbreviation='CusSrf'
        )

    def element_filter(self, element):
        """Accept only elements that support surface inspection."""
        try:
            return gom.api.custom_checks_util.is_surface_checkable(element)
        except (AttributeError, TypeError):
            return False

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        # Use gom.api.dialog directly so the element filter can be attached
        # before the dialog is displayed (Pattern B).
        dlg = gom.api.dialog.create(context, '/Custom_SurfaceInspection.gdlg')
        dlg.checked_element.filter = self.element_filter
        self.initialize_dialog(context, dlg, args)
        return self.apply_dialog(dlg, gom.api.dialog.show(context, dlg))

    def apply_dialog(self, dlg, result):
        """Extract dialog values and forward the tolerance to the framework."""
        params = super().apply_dialog(dlg, result)
        params['name'] = result['name']
        params['tolerance'] = result['tolerance']
        return params

    def compute_stage(self, context, values):
        """Compute the custom surface inspection element for one stage."""
        return _compute_surface_check(values, context.stage)


gom.run_api()
