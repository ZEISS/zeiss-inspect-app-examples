"""OSM map custom diagram contribution."""

import gom
from io import StringIO

import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
from gom import apicontribution
import gom.api.extensions.diagrams
import gom.api.extensions.diagrams.matplotlib_tools as mpltools
import gom.api.settings
import matplotlib.pyplot as plt
import numpy as np


@apicontribution
class OSMMapCustomDiagram(gom.api.extensions.diagrams.SVGDiagram):
    """Render custom location elements on OpenStreetMap tiles."""

    MIN_VIEW_WIDTH = 64
    MIN_VIEW_HEIGHT = 64
    MIN_VIEW_DPI = 72.0
    TILE_ZOOM_OFFSET = 2

    def __init__(self):
        super().__init__(
            id='com.zeiss.example.osm_map_custom_diagram',
            description='OSM Map Custom Diagram'
        )

    @staticmethod
    def _normalized_view(view):
        safe_view = dict(view)
        safe_view['width'] = max(int(safe_view.get('width', 0) or 0), OSMMapCustomDiagram.MIN_VIEW_WIDTH)
        safe_view['height'] = max(int(safe_view.get('height', 0) or 0), OSMMapCustomDiagram.MIN_VIEW_HEIGHT)
        safe_view['dpi'] = max(float(safe_view.get('dpi', 0.0) or 0.0), OSMMapCustomDiagram.MIN_VIEW_DPI)
        return safe_view

    @staticmethod
    def _zoom_level(delta):
        return int(np.clip(np.floor(np.log2(360) - np.log2(delta)), 0, 20))

    @staticmethod
    def _meters_to_degrees(distance):
        return distance * 360 / (2 * np.pi * 6400000)

    @staticmethod
    def _create_svg_string(fig):
        svg_buffer = StringIO()
        fig.savefig(svg_buffer, format='svg')
        return svg_buffer.getvalue()

    @staticmethod
    def _export_svg(fig, view):
        """Export SVG while preserving the figure's explicit layout margins."""
        return OSMMapCustomDiagram._create_svg_string(fig)

    def plot(self, view, element_data):
        safe_view = self._normalized_view(view)
        figure = mpltools.setup_plot(plt, safe_view)
        axis = figure.add_subplot(111, projection=cimgt.OSM().crs)
        figure.subplots_adjust(left=0.02, right=0.98, top=0.88, bottom=0.14)
        axis.set_position((0.03, 0.16, 0.94, 0.68))
        request = cimgt.OSM(cache=True)

        locations = [entry['data'] for entry in element_data]
        latitudes = [location['latitude'] for location in locations]
        longitudes = [location['longitude'] for location in locations]
        lat_center = (min(latitudes) + max(latitudes)) / 2
        lon_center = (min(longitudes) + max(longitudes)) / 2

        map_range = gom.api.settings.get('range')
        aspect = gom.api.settings.get('aspect')
        delta = self._meters_to_degrees(map_range)
        zoom = min(self._zoom_level(delta) + self.TILE_ZOOM_OFFSET, 19)
        longitude_delta = delta / np.cos(lat_center * np.pi / 180)
        panel_aspect = 0.94 * safe_view['width'] / (0.68 * safe_view['height'])
        map_aspect = max(float(aspect), panel_aspect)
        delta_lat = delta / map_aspect
        axis.set_extent([
            lon_center - longitude_delta,
            lon_center + longitude_delta,
            lat_center - delta_lat,
            lat_center + delta_lat
        ])
        axis.add_image(request, zoom)
        axis.set_aspect('equal', adjustable='box')
        axis.set_position((0.03, 0.16, 0.94, 0.68))

        marker_style = gom.api.settings.get('marker_style')
        marker_color = gom.api.settings.get('marker_color')
        marker_size = gom.api.settings.get('marker_size')
        altitude_text = gom.tr('Alt.')

        for location in locations:
            label = location['label']
            altitude = location['altitude']
            annotation = ''
            if label and altitude is not None:
                annotation = f"{label}\n{altitude_text}: {altitude}"
            elif label:
                annotation = label
            elif altitude is not None:
                annotation = f"{altitude_text}: {altitude}"

            latitude = location['latitude']
            longitude = location['longitude']
            if annotation:
                axis.annotate(
                    annotation,
                    xy=(longitude, latitude),
                    transform=ccrs.PlateCarree(),
                    xytext=(gom.api.settings.get('label_xoffset'), gom.api.settings.get('label_yoffset')),
                    textcoords='offset points',
                    bbox=dict(boxstyle='round', fc='0.8'),
                    arrowprops=dict(arrowstyle='->', shrinkA=5, shrinkB=5)
                )
            axis.scatter(
                longitude,
                latitude,
                transform=ccrs.PlateCarree(),
                marker=marker_style,
                s=marker_size,
                c=marker_color
            )

        axis.set_title(gom.api.settings.get('title'), pad=8)
        axis.text(
            0.99,
            0.01,
            '© OpenStreetMap contributors',
            transform=axis.transAxes,
            ha='right',
            va='bottom',
            fontsize=8,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2)
        )
        svg_string = self._export_svg(figure, safe_view)
        plt.close(figure)
        return svg_string


gom.run_api()
