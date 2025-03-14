# -*- coding: utf-8 -*-
#
# scripted_element_progress.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import time
#
# Dialog function
#
# This function will show the creation / editing dialog
#


def dialog(context, params):

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
                        "text": "Start Preview Calculation",
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
        "position": "",
        "size": {
            "height": 110,
            "width": 198
        },
        "sizemode": "",
        "style": "",
        "title": {
            "id": "",
            "text": "scripted_element_progress",
            "translatable": True
        }
    })

    def dlg_handler(widget):
        if widget == DIALOG.button:
            context.calc(params=params, dialog=DIALOG)

    DIALOG.handler = dlg_handler
    gom.script.sys.show_user_defined_dialog(dialog=DIALOG)

    params["test"] = "test"
    return params

#
# Calculation function
#


def calculation(context, params):
    # -------------------------------------------------------------------------
    limit = 100
    context.progress_stages_total = limit
    for i in range(limit):
        context.progress_stages_computing = i
        time.sleep(0.1)
    # -------------------------------------------------------------------------

    for s in context.stages:
        context.result[s] = (1.0, 0.0, 0.0)
    return True
