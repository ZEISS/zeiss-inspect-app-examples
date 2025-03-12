# -*- coding: utf-8 -*-
#
# widget_visibility.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom


# Setup dialog from file set list of items by script
def setup_dialog():

    DIALOG = gom.script.sys.create_user_defined_dialog(dialog={
        "content": [
            [
                {
                    "columns": 2,
                    "name": "label",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": "- Example dialog content",
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
                }
            ],
            [
                {
                    "columns": 1,
                    "name": "separator",
                    "rows": 1,
                    "title": {
                        "id": "",
                        "text": "More settings",
                        "translatable": True
                    },
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "separator"
                },
                {
                    "button_type": "toggle",
                    "columns": 1,
                    "icon": "AAAAAA==",
                    "icon_file_name": "",
                    "icon_size": {
                        "value": "icon"
                    },
                    "icon_system_size": {
                        "value": "default"
                    },
                    "icon_system_type": {
                        "value": "ok"
                    },
                    "icon_type": {
                        "value": "none"
                    },
                    "name": "button",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": ">",
                        "translatable": True
                    },
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "button::pushbutton"
                }
            ],
            [
                {
                    "columns": 2,
                    "name": "label_bottom",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": "I am visible",
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
                }
            ]
        ],
        "control": {
            "id": "OkCancel"
        },
        "embedding": "",
        "position": "",
        "size": {
            "height": 160,
            "width": 198
        },
        "sizemode": "",
        "style": "",
        "title": {
            "id": "",
            "text": "Example dialog",
            "translatable": True
        }
    })
    DIALOG.label_bottom.visible = False

    # -------------------------------------------------------------------------
    def dialog_event_handler(widget):
        if str(widget) == "system":
            return

        if widget == DIALOG.button:
            DIALOG.label_bottom.visible = not DIALOG.label_bottom.visible
    # -------------------------------------------------------------------------

    DIALOG.handler = dialog_event_handler
    return DIALOG


#
# Example execution
#
if __name__ == '__main__':
    DIALOG = setup_dialog()
    gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
