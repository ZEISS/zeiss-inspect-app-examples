"""
Custom nominal/actual Offset Point Element Example

Carl Zeiss GOM Metrology GmbH, 2026

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.extensions
import gom.api.extensions.actuals
import gom.api.extensions.nominals

from gom import apicontribution


def _get_base_point(base):
    """Get the position coordinate from a base element.

    Tries 'center_coordinate' first (points, spheres, …),
    then 'coordinate1' (cones, cylinders, …).
    Raises ValueError if neither attribute is accessible.
    """
    try:
        return base.center_coordinate
    except (AttributeError, TypeError):
        pass
    try:
        return base.coordinate1
    except (AttributeError, TypeError) as exc:
        raise ValueError(
            "Base element has no 'center_coordinate' or 'coordinate1' attribute!"
        ) from exc


def _has_point_coordinate(element):
    """Return True if element has a supported position coordinate attribute."""
    try:
        _ = element.center_coordinate
        return True
    except (AttributeError, TypeError):
        pass
    try:
        _ = element.coordinate1
        return True
    except (AttributeError, TypeError):
        return False

def generate_point_element(offset_x, offset_y, offset_z, base):
    """
    Generates an offset point

    Params:
        - base: gom point element with a 'center_coordinate' or 'coordinate1' attribute
        - offset_x: Float value of the offset in x-direction
        - offset_y: Float value of the offset in y-direction
        - offset_z: Float value of the offset in z-direction

    Returns:
        Dictionary with point-element data:
        {
            "value": (float(x-value), float(y-value), float(z-value)),
            "data":  {"offset_x": ..., "offset_y": ..., "offset_z": ...}
        }
    """
    if abs(offset_x) < 1 or abs(offset_y) < 1 or abs(offset_z) < 1:
        raise ValueError("Offset must be > 1 in either direction!")

    base_point = _get_base_point(base)

    return {
        "value": (
            float(base_point.x + offset_x),
            float(base_point.y + offset_y),
            float(base_point.z + offset_z)
        ),
        "data": {
            "offset_x": float(offset_x),
            "offset_y": float(offset_y),
            "offset_z": float(offset_z)
        }
    }


@apicontribution
class ActualPoint(gom.api.extensions.actuals.Point):
    """
    Bare minimum custom actual point element.

    Features:
    - Returns the base element's center coordinate as the point value (offset is ignored)
    """

    def __init__(self):
        """Register the custom actual point contribution."""
        super().__init__(
            id='examples.custom_actual_point_minimal',
            description='Custom Actual Point (Minimal)'
        )

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Point.gdlg')

    def compute_stage(self, _context, values):
        """Return the base element's center coordinate as the point value."""
        base_point = _get_base_point(values['base'])
        return {"value": (float(base_point.x), float(base_point.y), float(base_point.z))}


@apicontribution
class ActualOffsetPoint(gom.api.extensions.actuals.Point):
    """
    Custom actual point element with offset.

    Features:
    - Computes a point offset from a base element's center coordinate
    - Validates that each offset component is greater than 1;
      raises an error shown in the element properties
    - Stores offset values as custom element data tokens (offset_x, offset_y, offset_z)
    - Logs inputs and result via add_log_message()
    """

    def __init__(self):
        """Register the custom actual point contribution."""
        super().__init__(id='examples.custom_actual_point', description='Custom Actual Point')

    def dialog(self, context, args):
        """Show the creation dialog and return the user-provided parameters."""
        return self.show_dialog(context, args, '/Custom_Point.gdlg')

    def compute_stage(self, context, values):
        """Compute the actual offset point."""
        self.add_log_message(
            context, 'info',
            f"{values['offset_x']=}, {values['offset_y']=}, "
            f"{values['offset_z']=}, {values['base']=}"
        )
        result = generate_point_element(
            offset_x=values['offset_x'],
            offset_y=values['offset_y'],
            offset_z=values['offset_z'],
            base=values['base']
        )
        self.add_log_message(context, 'info', f"{result=}")
        return result


@apicontribution
class NominalOffsetPoint(gom.api.extensions.nominals.Point):
    """
    Custom nominal point element with offset.

    Features:
    - Computes a point offset from a base element's center coordinate
    - Validates that each offset component is greater than 1;
      raises an error shown in the element properties
    - Logs inputs and result via add_log_message()
    - (+) Widget filter on the base selector: only elements with 'center_coordinate'
      or 'coordinate1' are selectable
    - (+) Dialog event handler: shows a status hint until a valid base element is selected
    - (+) Triggers preview recomputation when a valid base element is selected
    """

    def __init__(self):
        """Register the custom nominal point contribution."""
        super().__init__(id='examples.custom_nominal_point', description='Custom Nominal Point')
        self.dlg = None

    def dialog(self, context, args):
        """
        Create dialog object and save it as attribute.
        Set a filter on the base widget so only elements with a
        'center_coordinate' or 'coordinate1' are selectable — the dialog manages the
        OK-button state automatically based on the filter result.
        Show dialog and return parameters.
        """
        self.dlg = gom.api.dialog.create(context, '/Custom_Point.gdlg')
        self.dlg.base.filter = _has_point_coordinate
        self.initialize_dialog(context, self.dlg, args)
        res = self.apply_dialog(self.dlg, gom.api.dialog.show(context, self.dlg))
        return res

    def compute_stage(self, context, values):
        """
        Compute the nominal point with offset.

        If offset values are too small, raise an error to be shown in
        the creation dialog and in the element properties.
        """
        self.add_log_message(context, 'info', f"{values['base']=}")
        result = generate_point_element(
            offset_x=values['offset_x'],
            offset_y=values['offset_y'],
            offset_z=values['offset_z'],
            base=values['base']
        )
        self.add_log_message(context, 'info', f"{result=}")
        return result

    def event(self, _context, event_type, parameters):
        """
        Show a status hint until a valid base is selected.
        Returns True to trigger a preview recomputation when one is.
        """
        if event_type == 'dialog::initialized':
            self.dlg.control.status = (
                "Select a base element with 'center_coordinate' or 'coordinate1'!"
            )

        if event_type == 'dialog::changed':
            base = parameters['values'].get('base')
            if base is not None and _has_point_coordinate(base):
                self.dlg.control.status = ''
                return True

        return False


gom.run_api()
