"""Interactive custom diagram example with point-cloud overlay."""

from io import StringIO

import gom
from gom import apicontribution

import gom.api.extensions.diagrams
import gom.api.extensions.diagrams.matplotlib_tools as mpltools
import matplotlib.pyplot as plt
from numpy.linalg import LinAlgError


@apicontribution
class DiagramWithPointCloudOverlay(gom.api.extensions.diagrams.SVGDiagram):
    """Interactive SVG diagram using point-based overlay interaction mapping."""

    INTERACTION_SCRIPT = 'testscript'
    INTERACTION_ARGS = {'name': 'testname', 'testval': 17.00351334}
    MARKER_SIZE = 120
    MARKER_COLOR = '#2f6fed'
    MARKER_ALPHA = 0.5
    MIN_VIEW_WIDTH = 64
    MIN_VIEW_HEIGHT = 64
    MIN_VIEW_DPI = 72.0

    def __init__(self):
        """Initialize service metadata for the point-cloud overlay diagram."""
        super().__init__(
            id='com.zeiss.example.custom_diagrams.point_cloud_overlay',
            description='Interactive Custom Diagram with Point Cloud Overlay'
        )

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

    @staticmethod
    def _normalized_view(view):
        """Guard against zero-sized embedded canvases in the diagram view."""
        safe_view = dict(view)
        safe_view['width'] = max(int(safe_view.get('width', 0) or 0), DiagramWithPointCloudOverlay.MIN_VIEW_WIDTH)
        safe_view['height'] = max(int(safe_view.get('height', 0) or 0), DiagramWithPointCloudOverlay.MIN_VIEW_HEIGHT)
        safe_view['dpi'] = max(float(safe_view.get('dpi', 0.0) or 0.0), DiagramWithPointCloudOverlay.MIN_VIEW_DPI)
        return safe_view

    @staticmethod
    def _create_svg_string(fig):
        """Export SVG directly to avoid matplotlib_tools tight_layout failures."""
        svg_buffer = StringIO()
        fig.savefig(svg_buffer, format='svg')
        return svg_buffer.getvalue()

    @staticmethod
    def _normalize_overlay_point(point_coords, view):
        """Convert overlay coordinates into plain relative floats in the range 0..1."""
        x_coord = float(point_coords[0])
        y_coord = float(point_coords[1])

        if x_coord > 1.0 or y_coord > 1.0:
            width = max(float(view.get('width', 0) or 0), 1.0)
            height = max(float(view.get('height', 0) or 0), 1.0)
            x_coord /= width
            y_coord /= height

        return (x_coord, y_coord)

    @staticmethod
    def _export_svg(fig, safe_view):
        """Prefer the ZEISS helper output, but fall back to direct matplotlib export."""
        try:
            return mpltools.create_svg(plt, safe_view)
        except (AttributeError, LinAlgError, RuntimeError, TypeError, ValueError) as error:
            gom.log.debug(f'Point cloud overlay falling back to direct SVG export: {error}')
            return DiagramWithPointCloudOverlay._create_svg_string(fig)

    def add_all_overlay_data(self, element_data, display_coords, view, overlay):
        """Populate point-based overlay entries using precomputed display coordinates."""
        for index, (element_entry, point_coords) in enumerate(zip(element_data, display_coords)):
            element_uuid, element_name = self._element_metadata(element_entry)
            interaction_point = self._normalize_overlay_point(point_coords, view)
            if index == 0:
                # Keep custom interaction on the first point only to demonstrate mixed interaction modes.
                self.add_element_to_overlay(
                    overlay,
                    element_uuid,
                    interaction_point,
                    element_name=element_name,
                    tooltip=f"{element_name}: radius = {element_entry['data']['radius']}",
                    custom_interaction=True
                )
            else:
                self.add_element_to_overlay(
                    overlay,
                    element_uuid,
                    interaction_point,
                    element_name=element_name,
                    tooltip=f"{element_name}: radius = {element_entry['data']['radius']}"
                )

    def event(self, element_name, element_uuid, event_data):
        """Handle custom click interaction for selected overlay points."""
        callback_args = dict(self.INTERACTION_ARGS)
        callback_args.update({
            'element_name': element_name,
            'element_uuid': element_uuid,
            'mouse': event_data
        })
        return self.finish_event(self.INTERACTION_SCRIPT, callback_args)

    @staticmethod
    def _radius_series(element_data):
        """Build x/y series from element radii for scatter plotting."""
        x_axis = []
        y_axis = []
        for index, entry in enumerate(element_data):
            x_axis.append(index)
            y_axis.append(entry['data']['radius'])
        return x_axis, y_axis

    def plot(self, view, element_data):
        """Render an interactive scatter plot with point-cloud overlay."""
        safe_view = self._normalized_view(view)
        fig = mpltools.setup_plot(plt, safe_view)
        ax = fig.gca()
        overlay = {}

        x_axis, y_axis = self._radius_series(element_data)
        points = list(zip(x_axis, y_axis))
        display_coords = mpltools.get_display_coords(ax, points, safe_view)

        # Point-cloud overlay maps interaction by display coordinates, so gid mapping is not needed here.
        for x_value, y_value in points:
            ax.scatter(
                x_value,
                y_value,
                s=self.MARKER_SIZE,
                c=self.MARKER_COLOR,
                alpha=self.MARKER_ALPHA
            )

        ax.set_title('Interactive Scatterplot with Point Cloud Overlay')
        ax.set_xlabel('Index')
        ax.set_ylabel('Radius')

        svg_string = self._export_svg(fig, safe_view)

        self.add_all_overlay_data(element_data, display_coords, safe_view, overlay)
        plt.close(fig)

        return self.finish_plot(svg_string, overlay)


gom.run_api()
