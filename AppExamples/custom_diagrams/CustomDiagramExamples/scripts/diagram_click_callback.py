"""Callback script used by custom diagram click events.

Carl Zeiss GOM Metrology GmbH, 2026

This App is part of the ZEISS INSPECT Python API Examples:
https://github.com/ZEISS/zeiss-inspect-app-examples
"""

import gom
import gom.api.inspection_details


def _safe_select_element(element_uuid):
    """Best-effort selection helper for interactive demo callbacks."""
    if not element_uuid:
        return
    try:
        gom.script.sys.select_elements_by_uuid(elements=[element_uuid])
    except Exception as error:
        gom.log.info(f'CustomDiagramExamples: could not select element by uuid: {error}')


def _request_diagram_refresh():
    """Refresh inspection details so diagram callbacks become visible immediately."""
    gom.api.inspection_details.refresh()


try:
    parameters: dict[str, object] = {}
    gom.read_parameters(parameters)
    callback_name = parameters.get('name', '<not provided>')
    callback_value = parameters.get('testval', '<not provided>')
    callback_uuid = parameters.get('element_uuid')

    gom.log.info(
        f'CustomDiagramExamples callback executed: {callback_name=}, {callback_value=}, {callback_uuid=}'
    )
    _safe_select_element(callback_uuid)
    _request_diagram_refresh()
except Exception as error:
    gom.log.info(f'CustomDiagramExamples callback failed: {error}')