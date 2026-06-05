"""
CustomCurveInspection Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples

Mirrors the functionality of the ScriptedCurveCheck example but uses the
modern gom.api.extensions.inspections.Curve API instead of the legacy
scripted element approach.

The check accepts any curve-checkable actual element and computes the
y-coordinate of each curve vertex as the deviation value. The nominal
reference is zero (the XZ-plane). This demonstrates how to create a
per-vertex curve inspection from a geometric element property.
"""

import gom
import gom.api.custom_checks_util
import gom.api.dialog
import gom.api.extensions
import gom.api.extensions.inspections
import numpy as np

from gom import apicontribution


def _compute_curve_check(values, stage):
    """
    Compute per-vertex deviation values for the curve inspection.

    For each vertex of the checked element, the y-coordinate is used as the
    deviation value. The nominal reference is 0.0 (distance from the XZ-plane).

    :param values: dict with key 'checked_element'
    :param stage:  current stage index (from context.stage)
    :returns: dict with 'actual_values', 'nominal_value', 'target_element', 'data'
    """
    element = values['checked_element']

    # -------------------------------------------------------------------------
    # Read the 3D vertex coordinates of the curve element for the current stage.
    # The result of element.data.coordinate is a staged array; indexing with the
    # stage retrieves only the (N, 3) vertex matrix for that stage.
    vertices = np.array(element.data.coordinate)[stage]

    # Use the y-coordinate of each vertex as the deviation value.
    # nominal_value = 0.0 means every vertex is expected to lie on the XZ-plane.
    actual_values = vertices[:, 1].tolist()
    # -------------------------------------------------------------------------

    return {
        'actual_values': actual_values,
        'nominal_value': 0.0,
        'target_element': element,
        'data': {
            'checked_element_name': element.name,
            'num_points': len(actual_values)
        }
    }


@apicontribution
class CustomCurveInspection(gom.api.extensions.inspections.Curve):
    """
    Custom curve inspection that measures the y-deviation along a curve.

    Features:
    - Element selector filtered to curve-checkable actual elements
    - Per-vertex deviation: actual_values[i] = vertex.y (distance from XZ-plane)
    - Nominal reference: 0.0 (common nominal for all vertices)
    - Custom tolerance dialog using the built-in tolerance widget
    - Data tokens: checked_element_name, num_points
    """

    def __init__(self):
        """Register the custom curve inspection contribution."""
        super().__init__(
            id='examples.custom_curve_inspection',
            description='Custom Curve Inspection',
            dimension='LENGTH',
            abbreviation='CusCrv'
        )

    def element_filter(self, element):
        """Accept only elements that support curve inspection."""
        try:
            return gom.api.custom_checks_util.is_curve_checkable(element)
        except (AttributeError, TypeError):
            return False

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        # Use gom.api.dialog directly so the element filter can be attached
        # before the dialog is displayed (Pattern B).
        dlg = gom.api.dialog.create(context, '/Custom_CurveInspection.gdlg')
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
        """Compute the custom curve inspection element for one stage."""
        return _compute_curve_check(values, context.stage)


gom.run_api()
