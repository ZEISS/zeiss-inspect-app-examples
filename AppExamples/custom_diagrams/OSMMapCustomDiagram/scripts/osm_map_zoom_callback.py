"""Callback for changing the OSM map zoom range.

Carl Zeiss GOM Metrology GmbH, 2026

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.settings


def _refresh_diagram():
    """Recompute setting-dependent location data and refresh the diagram."""
    gom.script.sys.recalculate_visible_elements_in_all_stages(enable=True)
    gom.script.sys.recalculate_project(with_reports=False)


try:
    parameters: dict[str, object] = {}
    gom.read_parameters(parameters)
    zoom_direction = parameters.get('direction')
    requested_range = parameters.get('range')
    if zoom_direction in ('in', 'out') and requested_range is not None:
        gom.api.settings.set('range', float(requested_range))
        _refresh_diagram()
except Exception as error:
    gom.log.info(f'OSMMapCustomDiagram zoom callback failed: {error}')
