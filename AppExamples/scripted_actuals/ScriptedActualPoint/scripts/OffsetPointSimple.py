# -*- coding: utf-8 -*-
#
# offset_point_simple.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom

# -------------------------------------------------------------------------


def dialog(context, params):

    DIALOG = gom.script.sys.create_user_defined_dialog(dialog={
        "content": [
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
            "height": 148,
            "width": 251
        },
        "sizemode": "",
        "style": "",
        "title": {
            "id": "",
            "text": "Simple offset point",
            "translatable": True
        }
    })

    if 'x' in params:
        DIALOG.i_x.value = params['x']
    if 'base' in params:
        DIALOG.point.value = params['base']

    RESULT = gom.script.sys.show_user_defined_dialog(dialog=DIALOG)

    params['x'] = DIALOG.i_x.value
    params['base'] = DIALOG.point.value

    context.name = 'My scripted point'
    return params
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------


def calculation(context, params):
    base = params['base'].center_coordinate
    context.result[0] = (base.x + params['x'], base.y, base.z)
    return True
# -------------------------------------------------------------------------
