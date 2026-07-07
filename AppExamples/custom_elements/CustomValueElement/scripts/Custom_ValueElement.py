"""
Custom nominal/actual Value Element Example

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
class ActualValueElement(gom.api.extensions.actuals.ValueElement):
    """
    Custom actual value element.

    Features:
    - Creates a scalar value element from a user-defined float value
    - Stores the square of the value as a custom element data token (value_squared)
    """

    def __init__(self):
        """Register the custom actual value element contribution."""
        super().__init__(
            id='examples.custom_actual_value_element',
            description='Custom Actual Value Element'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_ValueElement.gdlg')

    def compute(self, _context, values):
        """Compute the actual value element."""
        value = float(values['value'])
        return {
            "value": value,
            "data": {"value_squared": value * value}
        }


@apicontribution
class NominalValueElement(gom.api.extensions.nominals.ValueElement):
    """
    Custom nominal value element.

    Features:
    - Creates a scalar value element from a user-defined float value
    - Stores the square of the value as a custom element data token (value_squared)
    """

    def __init__(self):
        """Register the custom nominal value element contribution."""
        super().__init__(
            id='examples.custom_nominal_value_element',
            description='Custom Nominal Value Element'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_ValueElement.gdlg')

    def compute(self, _context, values):
        """Compute the nominal value element."""
        value = float(values['value'])
        return {
            "value": value,
            "data": {"value_squared": value * value}
        }


gom.run_api()
