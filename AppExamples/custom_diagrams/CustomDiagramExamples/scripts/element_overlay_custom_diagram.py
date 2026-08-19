"""Interactive custom diagram example with element overlay.

Carl Zeiss GOM Metrology GmbH, 2026

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

from io import StringIO

import gom
from gom import apicontribution

import gom.api.extensions.diagrams
import gom.api.extensions.diagrams.matplotlib_tools as mpltools
import matplotlib.pyplot as plt
from numpy.linalg import LinAlgError


@apicontribution
class DiagramWithElementOverlay(gom.api.extensions.diagrams.SVGDiagram):
    """Interactive SVG diagram with full-element overlay hitboxes and click callbacks."""

    INTERACTION_SCRIPT = 'diagram_click_callback'
    INTERACTION_ARGS = {'name': 'testname', 'testval': 17.00351334}
    RENDER_CONFIG = {'auto_generated_overlay_use': True}
    DEFAULT_MARKER_COLOR = '#4c956c'
    SELECTED_MARKER_COLOR = '#f45d48'
    MARKER_SIZE = 120
    MIN_VIEW_WIDTH = 64
    MIN_VIEW_HEIGHT = 64
    MIN_VIEW_DPI = 72.0

    def __init__(self):
        """Initialize service metadata for the element-overlay custom diagram."""
        super().__init__(
            id='com.zeiss.example.custom_diagrams.element_overlay',
            description='Interactive Custom Diagram with Element Overlay'
        )
        self.last_clicked_uuid = None

    @staticmethod
    def _radius_series(element_data):
        """Build x/y series from element radii for scatter plotting."""
        x_axis = []
        y_axis = []
        for index, entry in enumerate(element_data):
            x_axis.append(index)
            y_axis.append(entry['data']['radius'])
        return x_axis, y_axis

    @staticmethod
    def _element_metadata(element_entry):
        """Resolve the documented element reference into UUID and display name."""
        element = element_entry.get('element')
        element_uuid = element_entry.get('uuid')
        element_name = '<unnamed element>'

        if element is not None:
            element_name = getattr(element, 'name', str(element))
            element_getter = getattr(element, 'get', None)
            if not element_uuid and callable(element_getter):
                element_uuid = element_getter('uuid')

        return element_uuid, element_name

    def _marker_color(self, element_uuid):
        """Use a distinct color for the last clicked element."""
        if element_uuid and element_uuid == self.last_clicked_uuid:
            return self.SELECTED_MARKER_COLOR
        return self.DEFAULT_MARKER_COLOR

    @staticmethod
    def _normalized_view(view):
        """Guard against zero-sized embedded canvases in the diagram view."""
        safe_view = dict(view)
        safe_view['width'] = max(int(safe_view.get('width', 0) or 0), DiagramWithElementOverlay.MIN_VIEW_WIDTH)
        safe_view['height'] = max(int(safe_view.get('height', 0) or 0), DiagramWithElementOverlay.MIN_VIEW_HEIGHT)
        safe_view['dpi'] = max(float(safe_view.get('dpi', 0.0) or 0.0), DiagramWithElementOverlay.MIN_VIEW_DPI)
        return safe_view

    @staticmethod
    def _create_svg_string(fig):
        """Export SVG directly to avoid matplotlib_tools tight_layout failures."""
        svg_buffer = StringIO()
        fig.savefig(svg_buffer, format='svg')
        return svg_buffer.getvalue()

    @staticmethod
    def _export_svg(fig, safe_view):
        """Prefer the ZEISS helper output, but fall back to direct matplotlib export."""
        try:
            return mpltools.create_svg(plt, safe_view)
        except (AttributeError, LinAlgError, RuntimeError, TypeError, ValueError) as error:
            gom.log.debug(f'Element overlay falling back to direct SVG export: {error}')
            return DiagramWithElementOverlay._create_svg_string(fig)

    def add_all_overlay_data(self, element_data, overlay):
        """Populate overlay metadata for auto-generated full-element hitboxes."""
        for element_entry in element_data:
            element_uuid, element_name = self._element_metadata(element_entry)
            self.add_element_to_overlay(
                overlay,
                element_uuid,
                (0, 0),
                element_name=element_name,
                tooltip=f"{element_name}: radius = {element_entry['data']['radius']}",
                custom_interaction=True
            )

    def event(self, element_name, element_uuid, event_data):
        """Handle custom click interaction for overlay-mapped elements."""
        self.last_clicked_uuid = element_uuid
        callback_args = dict(self.INTERACTION_ARGS)
        callback_args.update({
            'element_name': element_name,
            'element_uuid': element_uuid,
            'mouse': event_data
        })
        return self.finish_event(self.INTERACTION_SCRIPT, callback_args)

    def plot(self, view, element_data):
        """Render an interactive scatter plot with full-element overlay."""
        safe_view = self._normalized_view(view)
        fig = mpltools.setup_plot(plt, safe_view)
        ax = fig.gca()

        overlay = {}
        x_axis, y_axis = self._radius_series(element_data)

        # Element overlay uses gid to map each plotted marker to its element UUID.
        for x_value, y_value, element_entry in zip(
            x_axis,
            y_axis,
            element_data
        ):
            element_uuid, _element_name = self._element_metadata(element_entry)
            scatter_kwargs = {
                's': self.MARKER_SIZE,
                'c': self._marker_color(element_uuid),
                'alpha': 0.85
            }
            if element_uuid:
                scatter_kwargs['gid'] = self.get_overlay_tag(element_uuid)

            ax.scatter(
                x_value,
                y_value,
                **scatter_kwargs
            )

        ax.set_title('Interactive Scatterplot with Element Overlay')
        ax.set_xlabel('Index')
        ax.set_ylabel('Radius')

        svg_string = self._export_svg(fig, safe_view)

        self.add_all_overlay_data(element_data, overlay)
        plt.close(fig)

        return self.finish_plot(svg_string, overlay, self.RENDER_CONFIG)


gom.run_api()
