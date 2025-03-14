# -*- coding: utf-8 -*-
#
# unit_dialog_event_handler.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---


import gom

# Setting up a dialog with event handler
# which links units of unit and tolerance widget


def setup_dialog():
    DIALOG = gom.script.sys.create_user_defined_dialog(dialog={
        "content": [
            [
                {
                    "columns": 1,
                    "name": "unit",
                    "rows": 1,
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "input::unit",
                    "value": "UNIT_NONE"
                }
            ],
            [
                {
                    "background_style": "",
                    "columns": 1,
                    "maximum": 1000,
                    "minimum": 0,
                    "name": "input",
                    "precision": 2,
                    "rows": 1,
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "input::number",
                    "unit": "UNIT_NONE",
                    "value": 0
                }
            ],
            [
                {
                    "columns": 1,
                    "expanded": True,
                    "link_limits": True,
                    "lower": 0,
                    "lower_warn": 0,
                    "mode": "no_tolerance",
                    "name": "tolerances",
                    "rows": 1,
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "tolerances",
                    "unit": "UNIT_NONE",
                    "upper": 0,
                    "upper_warn": 0,
                    "use_warn_limit": False
                }
            ]
        ],
        "control": {
            "id": "OkCancel"
        },
        "embedding": "",
        "position": "",
        "size": {
            "height": 295,
            "width": 437
        },
        "sizemode": "",
        "style": "",
        "title": {
            "id": "",
            "text": "Unit widgets example",
            "translatable": True
        }
    })

    def dialog_event_handler(widget):
        if str(widget) == "system":
            return
        # -------------------------------------------------------------------------
        if widget == DIALOG.unit:
            DIALOG.input.unit = DIALOG.unit.value
            DIALOG.tolerances.unit = DIALOG.unit.value
        # -------------------------------------------------------------------------

    DIALOG.handler = dialog_event_handler
    return DIALOG


#
# Example execution
#
if __name__ == '__main__':
    DIALOG = setup_dialog()
    gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    print("Selected unit", DIALOG.unit.value)
