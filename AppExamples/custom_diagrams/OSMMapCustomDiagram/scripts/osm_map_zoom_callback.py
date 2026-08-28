"""Callback for changing the OSM map zoom range."""

import gom
import gom.api.settings


def _refresh_diagram():
    """Force recalculation because App settings are not project dependencies."""
    try:
        gom.script.sys.recalculate_visible_elements_in_all_stages(enable=True)
        gom.script.sys.recalculate_project(with_reports=False)
    except Exception as error:
        gom.log.info(f'OSMMapCustomDiagram recalculation failed: {error}')


def _select_elements(element_uuids):
    """Reselect contributing elements so Inspection Details reloads its diagram."""
    if not element_uuids:
        return
    try:
        gom.script.sys.select_elements_by_uuid(elements=element_uuids)
    except Exception as error:
        gom.log.info(f'OSMMapCustomDiagram element selection failed: {error}')


try:
    gom.read_parameters(globals())
    zoom_direction = globals().get('direction')
    requested_range = globals().get('range')
    if zoom_direction in ('in', 'out') and requested_range is not None:
        gom.api.settings.set('range', float(requested_range))
        _select_elements(globals().get('element_uuids'))
        _refresh_diagram()
except Exception as error:
    gom.log.info(f'OSMMapCustomDiagram zoom callback failed: {error}')
