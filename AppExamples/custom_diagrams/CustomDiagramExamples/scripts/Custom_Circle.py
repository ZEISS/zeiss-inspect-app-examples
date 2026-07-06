"""Custom element used as data source for the custom diagram examples."""

import gom
import gom.api.extensions.actuals
import gom.api.extensions.nominals

from gom import apicontribution


def _attach_diagrams(contribution, results_states, bindings):
    """Attach the same stage-0 result to each configured diagram contribution id."""
    stage_zero_result = results_states['results'][0]
    diagram_data = []

    for _diagram_name, service_name in bindings:
        contribution.add_diagram_data(
            diagram_data=diagram_data,
            diagram_id='SVGDiagram',
            service_id=service_name,
            element_data=stage_zero_result
        )

    results_states['diagram_data'] = diagram_data
    return results_states


@apicontribution
class MyActualCircle(gom.api.extensions.actuals.Circle):
    """Actual circle contribution that publishes payloads to all diagram examples."""

    DIAGRAM_BINDINGS = [
        (
            'Basic Custom Diagram',
            'com.zeiss.example.custom_diagrams.basic'
        ),
        (
            'Interactive Custom Diagram with Element Overlay',
            'com.zeiss.example.custom_diagrams.element_overlay'
        ),
        (
            'Interactive Custom Diagram with Point Cloud Overlay',
            'com.zeiss.example.custom_diagrams.point_cloud_overlay'
        )
    ]

    def __init__(self):
        """Register the custom actual circle contribution used by diagram examples."""
        super().__init__(
            id='examples.custom_diagrams.actual_circle',
            description='Custom Actual Circle for Diagram Examples'
        )

    def dialog(self, context, args):
        """Open the input dialog for center, direction, and radius values."""
        return self.show_dialog(context, args, '/Custom_Circle.gdlg')

    def compute(self, _context, values):
        """Compute circle geometry from dialog values."""
        center = (
            float(values['center_x']),
            float(values['center_y']),
            float(values['center_z'])
        )
        direction = (
            float(values['dir_x']),
            float(values['dir_y']),
            float(values['dir_z'])
        )
        radius = float(values['radius'])

        return {
            'center': center,
            'direction': direction,
            'radius': radius,
            'data': {
                'center': center,
                'direction': direction,
                'radius': radius
            }
        }

    def finish(self, _context, results_states):
        """Map stage-0 element results to all diagram services in this app."""
        return _attach_diagrams(self, results_states, self.DIAGRAM_BINDINGS)


@apicontribution
class MyNominalCircle(gom.api.extensions.nominals.Circle):
    """Nominal circle contribution so the element is available in Construct workflows."""

    def __init__(self):
        """Register the custom nominal circle contribution used by diagram examples."""
        super().__init__(
            id='examples.custom_diagrams.nominal_circle',
            description='Custom Nominal Circle for Diagram Examples'
        )

    def dialog(self, context, args):
        """Open the input dialog for center, direction, and radius values."""
        return self.show_dialog(context, args, '/Custom_Circle.gdlg')

    def compute(self, _context, values):
        """Compute nominal circle geometry from dialog values."""
        center = (
            float(values['center_x']),
            float(values['center_y']),
            float(values['center_z'])
        )
        direction = (
            float(values['dir_x']),
            float(values['dir_y']),
            float(values['dir_z'])
        )
        radius = float(values['radius'])

        return {
            'center': center,
            'direction': direction,
            'radius': radius,
            'data': {
                'center': center,
                'direction': direction,
                'radius': radius
            }
        }

    def finish(self, _context, results_states):
        """Map stage-0 nominal results to all diagram services in this app."""
        return _attach_diagrams(self, results_states, MyActualCircle.DIAGRAM_BINDINGS)

gom.run_api()
