# -*- coding: utf-8 -*-
#
# script_icon_from_file.py
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/
# ---

import gom

# This script does nothing special. It's only purpose is to show how
# icons can be set to scripts and scripts can be put into the menu.
#
# For details, see:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.htmlscript_icons/script_icon_from_file.html

RESULT = gom.script.sys.execute_user_defined_dialog(dialog={
    "content": [
        [
            {
                "columns": 1,
                "name": "label",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "Hello from script with icon in menu.",
                    "translatable": True
                },
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "label",
                "word_wrap": False
            }
        ]
    ],
    "control": {
        "id": "Close"
    },
    "embedding": "",
    "position": "",
    "size": {
        "height": 102,
        "width": 227
    },
    "sizemode": "",
    "style": "",
    "title": {
        "id": "",
        "text": "Icon Script",
        "translatable": True
    }
})
