"""
CustomScalarInspection Element Example

Carl Zeiss GOM Metrology GmbH, 2027

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples

Mirrors the functionality of the ScriptedScalarCheck example but uses the
modern gom.api.extensions.inspections.Scalar API instead of the legacy
scripted element approach.

The check accepts any cylindrical or circular actual element and reads its
measured diameter, comparing it against a user-defined nominal. This
demonstrates how to compute a scalar inspection value from a geometric
property of an actual element.
"""

import gom
import gom.api.custom_checks_util
import gom.api.dialog
import gom.api.extensions
import gom.api.extensions.inspections

from gom import apicontribution


def _compute_scalar_check(values):
    """
    Compute a scalar inspection result for the selected element.

    :param values: dict with keys 'checked_element' and 'nominal'
    :returns: dict with 'nominal', 'actual', 'target_element', and 'data'
    :raises ValueError: if the element has no diameter property
    """
    element = values['checked_element']
    nominal = float(values['nominal'])

    # -------------------------------------------------------------------------
    # Read the actual diameter of the selected element.
    # Replace 'diameter' with another property for different element types,
    # e.g. 'radius', 'length', or 'center_in_local.x'.
    try:
        actual = float(element.diameter)
    except (AttributeError, TypeError) as exc:
        raise ValueError(
            f"Element '{element.name}' has no diameter property. "
            "Select a cylindrical or circular actual element."
        ) from exc
    # -------------------------------------------------------------------------

    return {
        'nominal': nominal,
        'actual': actual,
        'target_element': element,
        'data': {
            'checked_element_name': element.name
        }
    }


@apicontribution
class CustomScalarInspection(gom.api.extensions.inspections.Scalar):
    """
    Custom scalar inspection that re-evaluates an existing check's deviation.

    Features:
    - Element selector filtered to scalar-checkable inspection elements
    - Custom tolerance dialog using the built-in tolerance widget
    - Data token: checked_element_name (name of the inspected element)
    """

    def __init__(self):
        """Register the custom scalar inspection contribution."""
        super().__init__(
            id='examples.custom_scalar_inspection',
            description='Custom Scalar Inspection',
            dimension='LENGTH',
            abbreviation='CusSca'
        )

    def element_filter(self, element):
        """Accept only elements that support scalar inspection."""
        try:
            return gom.api.custom_checks_util.is_scalar_checkable(element)
        except (AttributeError, TypeError):
            return False

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        # Use gom.api.dialog directly so the element filter can be attached
        # before the dialog is displayed (Pattern B).
        dlg = gom.api.dialog.create(context, '/Custom_ScalarInspection.gdlg')
        dlg.checked_element.filter = self.element_filter
        self.initialize_dialog(context, dlg, args)
        return self.apply_dialog(dlg, gom.api.dialog.show(context, dlg))

    def apply_dialog(self, dlg, result):
        """Extract dialog values and forward the tolerance to the framework."""
        params = super().apply_dialog(dlg, result)
        params['name'] = result['name']
        params['tolerance'] = result['tolerance']
        return params

    def compute(self, _context, values):
        """Compute the custom scalar inspection element for one stage."""
        return _compute_scalar_check(values)


gom.run_api()
