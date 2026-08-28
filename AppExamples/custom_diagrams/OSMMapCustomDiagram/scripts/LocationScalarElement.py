"""Custom value element used as the OSM map diagram data source."""

import gom
import gom.api.extensions.actuals
import gom.api.settings

from gom import apicontribution


@apicontribution
class OSMMapLocation(gom.api.extensions.actuals.ValueElement):
    """Custom value element that publishes geolocation data to the OSM diagram."""

    DIAGRAM_ID = 'com.zeiss.example.osm_map_custom_diagram'

    def __init__(self):
        """Register the custom value element contribution."""
        super().__init__(
            id='examples.osm_map_custom_diagram.location',
            description='OSM Map Location'
        )

    def dialog(self, context, args):
        """Open the geolocation input dialog and restore previous values."""
        if not args.get('values'):
            # Let the element-name widget generate GeoLocation 1, GeoLocation 2, etc.
            args = dict(args)
            args.pop('name', None)
        return self.show_dialog(context, args, '/LocationScalarElement.gdlg')

    def compute(self, _context, values):
        """Validate geolocation values and return the diagram payload."""
        map_range = float(gom.api.settings.get('range'))
        latitude = float(values['lat'])
        longitude = float(values['lon'])
        altitude_enabled = bool(values.get('en_alt'))
        altitude = float(values['alt']) if altitude_enabled else None

        if not -90.0 <= latitude <= 90.0:
            raise ValueError('Latitude must be between -90 and 90 degrees')
        if not -180.0 <= longitude <= 180.0:
            raise ValueError('Longitude must be between -180 and 180 degrees')

        name = values.get('name', 'GeoLocation')
        label = values.get('label', '')
        return {
            'value': map_range,
            'name': name,
            'latitude': latitude,
            'longitude': longitude,
            'altitude': altitude,
            'altitude_enabled': altitude_enabled,
            'label': label,
            'data': {
                'name': name,
                'latitude': latitude,
                'longitude': longitude,
                'altitude': altitude,
                'altitude_enabled': altitude_enabled,
                'label': label,
                'map_range': map_range
            }
        }

    def finish(self, _context, results_states):
        """Attach the computed element result to the OSM map diagram."""
        diagram_data = []
        self.add_diagram_data(
            diagram_data=diagram_data,
            diagram_id='SVGDiagram',
            service_id=self.DIAGRAM_ID,
            element_data=results_states['results'][0]
        )
        results_states['diagram_data'] = diagram_data
        return results_states


gom.run_api()
