# -*- coding: utf-8 -*-
#
# offset_point_v2.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import time
import numpy as np


def dialog(context, params):

    DIALOG = gom.script.sys.create_user_defined_dialog(dialog={
        "content": [
            [
                {
                    "columns": 1,
                    "name": "label_3",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": "Name",
                        "translatable": True
                    },
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "label",
                    "word_wrap": False
                },
                {
                    "basename": {
                        "id": "",
                        "text": "Offset point",
                        "translatable": True
                    },
                    "columns": 1,
                    "mode": "manually",
                    "name": "name",
                    "numbering": True,
                    "read_only": False,
                    "rows": 1,
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "input::elementname"
                }
            ],
            [
                {
                    "columns": 1,
                    "name": "label",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": "X Offset",
                        "translatable": True
                    },
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "label",
                    "word_wrap": False
                },
                {
                    "background_style": "",
                    "columns": 1,
                    "maximum": 1000,
                    "minimum": 0,
                    "name": "i_x",
                    "precision": 2,
                    "rows": 1,
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "input::number",
                    "unit": "LENGTH",
                    "value": 0
                }
            ],
            [
                {
                    "columns": 1,
                    "name": "label_1",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": "Y Offset",
                        "translatable": True
                    },
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "label",
                    "word_wrap": False
                },
                {
                    "background_style": "",
                    "columns": 1,
                    "maximum": 1000,
                    "minimum": 0,
                    "name": "i_y",
                    "precision": 2,
                    "rows": 1,
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "input::number",
                    "unit": "LENGTH",
                    "value": 0
                }
            ],
            [
                {
                    "columns": 1,
                    "name": "label_2",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": "Z Offset",
                        "translatable": True
                    },
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "label",
                    "word_wrap": False
                },
                {
                    "background_style": "",
                    "columns": 1,
                    "maximum": 1000,
                    "minimum": 0,
                    "name": "i_z",
                    "precision": 2,
                    "rows": 1,
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "input::number",
                    "unit": "LENGTH",
                    "value": 0
                }
            ],
            [
                {
                    "columns": 1,
                    "name": "elem",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": "Base point",
                        "translatable": True
                    },
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "label",
                    "word_wrap": False
                },
                {
                    "columns": 1,
                    "fast_filter": False,
                    "name": "point",
                    "rows": 1,
                    "supplier": "any",
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "input::point3d"
                }
            ]
        ],
        "control": {
            "id": "OkCancel"
        },
        "embedding": "",
        "position": "",
        "size": {
            "height": 253,
            "width": 251
        },
        "sizemode": "",
        "style": "",
        "title": {
            "id": "",
            "text": "Offset Point v2",
            "translatable": True
        }
    })

    if 'x' in params:
        DIALOG.i_x.value = params['x']
    if 'y' in params:
        DIALOG.i_y.value = params['y']
    if 'z' in params:
        DIALOG.i_z.value = params['z']
    if 'base' in params:
        DIALOG.point.value = params['base']
    # Get previous element name, when started from "Edit creation"
    if len(params) > 0:
        DIALOG.name.value = context.name

    # -------------------------------------------------------------------------
    def dialog_event_handler(widget):
        # No treatment of system events
        if str(widget) == 'system':
            return
        # If preview calculation returned with error
        if str(widget) == 'error':
            DIALOG.control.status = context.error
            return
        # If preview calculation was successful
        if str(widget) == 'calculated':
            DIALOG.control.status = ''
            DIALOG.control.ok.enabled = True
            # Setting some display properties so the point is more visible

            return

        # All other changes in the dialog --> calculate preview
        params['x'] = DIALOG.i_x.value
        params['y'] = DIALOG.i_y.value
        params['z'] = DIALOG.i_z.value
        params['base'] = DIALOG.point.value
        context.name = DIALOG.name.value
        DIALOG.control.ok.enabled = False
        context.calc(params=params, dialog=DIALOG)

    DIALOG.handler = dialog_event_handler
    # -------------------------------------------------------------------------
    RESULT = gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    return params

# -------------------------------------------------------------------------


def calculation(context, params):
    valid_results = False
    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            base = params['base'].in_stage[stage].center_coordinate
            context.result[stage] = (base.x + params['x'], base.y + params['y'], base.z + params['z'])
            context.data[stage] = {"ude_mykey": 123456}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
