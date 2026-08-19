"""Follow-up script used by custom diagram click events."""

import gom


def _safe_select_element(element_uuid):
    """Best-effort selection helper for interactive demo callbacks."""
    if not element_uuid:
        return
    try:
        gom.script.sys.select_elements_by_uuid(elements=[element_uuid])
    except Exception as error:
        gom.log.info(f'CustomDiagramExamples: could not select element by uuid: {error}')


def _request_diagram_refresh():
    """Best-effort refresh so diagram callbacks become visible immediately."""
    try:
        gom.script.sys.recalculate_visible_elements_in_all_stages(enable=True)
        gom.script.sys.recalculate_project(with_reports=False)
    except Exception as error:
        gom.log.info(f'CustomDiagramExamples: could not refresh diagram view: {error}')


try:
    # Parameters are passed by finish_event and exposed as globals by ZEISS INSPECT.
    callback_name = globals().get('name', '<not provided>')
    callback_value = globals().get('testval', '<not provided>')
    callback_uuid = globals().get('element_uuid', None)

    gom.log.info(
        f'CustomDiagramExamples callback executed: {callback_name=}, {callback_value=}, {callback_uuid=}'
    )
    _safe_select_element(callback_uuid)
    _request_diagram_refresh()
except Exception as error:
    gom.log.info(f'CustomDiagramExamples callback failed: {error}')