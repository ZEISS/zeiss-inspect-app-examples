"""OSM map custom diagram contribution.

Carl Zeiss GOM Metrology GmbH, 2026

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

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
from matplotlib.patches import FancyBboxPatch


@apicontribution
class OSMMapCustomDiagram(gom.api.extensions.diagrams.SVGDiagram):
    """Render custom location elements on OpenStreetMap tiles."""

    ZOOM_CONTROL_LEFT = 0.94
    ZOOM_CONTROL_RIGHT = 0.98
    ZOOM_CONTROL_CENTER = 0.96
    ZOOM_CONTROL_SPLIT = 0.89
    MIN_VIEW_WIDTH = 64
    MIN_VIEW_HEIGHT = 64
    MIN_VIEW_DPI = 72.0
    TILE_ZOOM_OFFSET = 2

    def __init__(self):
        super().__init__(
            id='com.zeiss.example.osm_map_custom_diagram',
            description='OSM Map Custom Diagram'
        )
        self.refresh_element_uuids = []
        self.zoom_control_split_y = None

    @staticmethod
    def _element_uuid(element_entry):
        element_uuid = element_entry.get('uuid')
        element = element_entry.get('element')
        element_getter = getattr(element, 'get', None)
        if not element_uuid and callable(element_getter):
            element_uuid = element_getter('uuid')
        return element_uuid

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
    def _export_svg(fig, _view):
        """Export SVG while preserving the figure's explicit layout margins."""
        return OSMMapCustomDiagram._create_svg_string(fig)

    @staticmethod
    def _overlay_point(axis, x_coord, y_coord, view):
        """Convert axes-relative coordinates into normalized diagram coordinates."""
        display_point = axis.transAxes.transform((x_coord, y_coord))
        return (
            float(display_point[0]) / view['width'],
            1.0 - float(display_point[1]) / view['height']
        )

    def _draw_zoom_controls(self, axis, view, overlay, interaction_uuid):
        """Draw fixed zoom controls and register their interaction hitboxes."""
        axis.add_patch(
            FancyBboxPatch(
                (self.ZOOM_CONTROL_LEFT, 0.81),
                self.ZOOM_CONTROL_RIGHT - self.ZOOM_CONTROL_LEFT,
                0.16,
                transform=axis.transAxes,
                boxstyle='round,pad=0.004,rounding_size=0.012',
                facecolor='white',
                edgecolor='#555555',
                linewidth=0.8,
                alpha=0.94,
                zorder=20,
                clip_on=False
            )
        )
        axis.plot(
            [self.ZOOM_CONTROL_LEFT, self.ZOOM_CONTROL_RIGHT],
            [self.ZOOM_CONTROL_SPLIT, self.ZOOM_CONTROL_SPLIT],
            transform=axis.transAxes,
            color='#b0b0b0',
            linewidth=0.7,
            zorder=21,
            clip_on=False
        )
        split_point = self._overlay_point(
            axis,
            self.ZOOM_CONTROL_CENTER,
            self.ZOOM_CONTROL_SPLIT,
            view
        )
        self.zoom_control_split_y = split_point[1] * view['height']
        for symbol, y_coord in (('+', 0.93), ('-', 0.85)):
            axis.text(
                self.ZOOM_CONTROL_CENTER,
                y_coord,
                symbol,
                transform=axis.transAxes,
                ha='center',
                va='center',
                fontsize=14,
                fontweight='bold',
                color='black',
                zorder=20
            )
            self.add_element_to_overlay(
                overlay,
                interaction_uuid,
                self._overlay_point(axis, self.ZOOM_CONTROL_CENTER, y_coord, view),
                element_name='Map zoom',
                tooltip='Map zoom',
                custom_interaction=True
            )

    def event(self, _element_name, element_uuid, event_data):
        """Handle a zoom-control click and request a range update."""
        if element_uuid not in self.refresh_element_uuids or self.zoom_control_split_y is None:
            return None
        mouse_position = event_data.get('mouse_position', {})
        mouse_y = mouse_position.get('y')
        if mouse_y is None:
            return None
        direction = 'in' if float(mouse_y) < self.zoom_control_split_y else 'out'
        current_range = float(gom.api.settings.get('range'))
        updated_range = current_range / 2 if direction == 'in' else current_range * 2
        updated_range = min(1000000.0, max(100.0, updated_range))
        return self.finish_event(
            'osm_map_zoom_callback',
            {
                'direction': direction,
                'range': updated_range,
                'element_uuids': self.refresh_element_uuids
            }
        )

    def plot(self, view, element_data):
        safe_view = self._normalized_view(view)
        request = cimgt.OSM(
            cache=True,
            user_agent='ZEISS-INSPECT-OSMMapCustomDiagram/1.0 (+https://github.com/ZEISS/zeiss-inspect-app-examples)'
        )
        figure = mpltools.setup_plot(plt, safe_view)
        axis = figure.add_subplot(111, projection=request.crs)
        overlay = {}
        figure.subplots_adjust(left=0.02, right=0.98, top=0.88, bottom=0.14)
        axis.set_position((0.03, 0.16, 0.94, 0.68))

        locations = [entry['data'] for entry in element_data]
        self.refresh_element_uuids = [
            element_uuid
            for entry in element_data
            if (element_uuid := self._element_uuid(entry))
        ]
        latitudes = [location['latitude'] for location in locations]
        longitudes = [location['longitude'] for location in locations]
        lat_center = (min(latitudes) + max(latitudes)) / 2
        lon_center = (min(longitudes) + max(longitudes)) / 2

        map_range = float(locations[0].get('map_range', gom.api.settings.get('range')))
        aspect = gom.api.settings.get('aspect')
        delta = self._meters_to_degrees(map_range)
        zoom = min(self._zoom_level(delta) + self.TILE_ZOOM_OFFSET, 19)
        longitude_delta = delta / np.cos(lat_center * np.pi / 180)
        panel_aspect = 0.94 * safe_view['width'] / (0.68 * safe_view['height'])
        map_aspect = max(float(aspect), panel_aspect)
        delta_lat = delta / map_aspect
        extent = [
            lon_center - longitude_delta,
            lon_center + longitude_delta,
            lat_center - delta_lat,
            lat_center + delta_lat
        ]
        axis.set_extent(extent)
        axis.add_image(request, zoom)
        axis.set_aspect('equal', adjustable='box')
        axis.set_position((0.03, 0.16, 0.94, 0.68))
        axis.set_extent(extent)

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
        self._draw_zoom_controls(axis, safe_view, overlay, self.refresh_element_uuids[0])
        svg_string = self._export_svg(figure, safe_view)
        plt.close(figure)
        return self.finish_plot(svg_string, overlay)


gom.run_api()
