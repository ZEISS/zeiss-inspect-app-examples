"""Basic static custom diagram example."""

from io import StringIO

import gom
from gom import apicontribution

import gom.api.extensions.diagrams
import gom.api.extensions.diagrams.matplotlib_tools as mpltools
import matplotlib.pyplot as plt
from numpy.linalg import LinAlgError


@apicontribution
class MyBasicDiagram(gom.api.extensions.diagrams.SVGDiagram):
    """Static SVG diagram contribution that plots circle radius by index."""

    MIN_VIEW_WIDTH = 64
    MIN_VIEW_HEIGHT = 64
    MIN_VIEW_DPI = 72.0

    def __init__(self):
        """Initialize the basic custom diagram service metadata."""
        super().__init__(
            id='com.zeiss.example.custom_diagrams.basic',
            description='Basic Custom Diagram'
        )

    @staticmethod
    def _radius_series(element_data):
        """Extract index and radius arrays from element data."""
        indices = []
        radii = []
        for index, entry in enumerate(element_data):
            indices.append(index)
            radii.append(entry['data']['radius'])
        return indices, radii

    @staticmethod
    def _draw_plot(ax, indices, radii):
        """Draw the line chart for the basic radius plot."""
        ax.plot(indices, radii, marker='o', linestyle='-', linewidth=1.5)
        ax.set_title('Basic Diagram')
        ax.set_xlabel('Index')
        ax.set_ylabel('Radius')

    @staticmethod
    def _normalized_view(view):
        """Guard against zero-sized embedded canvases in the diagram view."""
        safe_view = dict(view)
        safe_view['width'] = max(int(safe_view.get('width', 0) or 0), MyBasicDiagram.MIN_VIEW_WIDTH)
        safe_view['height'] = max(int(safe_view.get('height', 0) or 0), MyBasicDiagram.MIN_VIEW_HEIGHT)
        safe_view['dpi'] = max(float(safe_view.get('dpi', 0.0) or 0.0), MyBasicDiagram.MIN_VIEW_DPI)
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
            gom.log.debug(f'Basic diagram falling back to direct SVG export: {error}')
            return MyBasicDiagram._create_svg_string(fig)

    def plot(self, view, element_data):
        """Render a simple radius-over-index line plot."""
        safe_view = self._normalized_view(view)
        fig = mpltools.setup_plot(plt, safe_view)
        ax = fig.gca()

        indices, radii = self._radius_series(element_data)
        self._draw_plot(ax, indices, radii)

        svg_string = self._export_svg(fig, safe_view)
        plt.close(fig)
        return svg_string


gom.run_api()
