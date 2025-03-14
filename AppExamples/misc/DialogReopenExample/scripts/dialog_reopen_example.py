# -*- coding: utf-8 -*-
#
# dialog_reopen_example.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom


def setup_dialog():
    DIALOG = gom.script.sys.create_user_defined_dialog(dialog={
        "content": [
            [
                {
                    "button_type": "push",
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
                        "text": "Close and reopen",
                        "translatable": True
                    },
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "button::pushbutton"
                }
            ]
        ],
        "control": {
            "id": "OkCancel"
        },
        "embedding": "",
        "position": "center",
        "size": {
            "height": 110,
            "width": 198
        },
        "sizemode": "",
        "style": "",
        "title": {
            "id": "",
                    "text": "Dialog Title",
                    "translatable": True
        }
    })
    # Dialog event handler
    # On button press, dialog is closed but reopen is set to True

    def dialog_event_handler(widget):
        global reopen

        if str(widget) == "initialize":
            reopen = False

        # -------------------------------------------------------------------------
        if widget == DIALOG.button:
            gom.script.sys.close_user_defined_dialog(dialog=DIALOG)
            gom.script.sys.delay_script(time=1)  # Do stuff while dialog is closed
            reopen = True
        # -------------------------------------------------------------------------
    DIALOG.handler = dialog_event_handler
    return DIALOG


#
# Example execution
#
if __name__ == '__main__':
    # Main function, will (re)open the dialog as often as required
    DIALOG = setup_dialog()
    # Variable guarding the reopen mechanism
    # -------------------------------------------------------------------------
    reopen = True
    while reopen:
        gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    # -------------------------------------------------------------------------
