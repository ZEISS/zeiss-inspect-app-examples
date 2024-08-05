# -*- coding: utf-8 -*-
#
# listdir_dialog.py
#
# List files in a directory
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import os


RESULT=gom.script.sys.execute_user_defined_dialog (dialog={
    "content": [
        [
            {
                "columns": 1,
                "default": "",
                "file_types": [
                ],
                "file_types_default": "",
                "limited": False,
                "name": "directory",
                "rows": 1,
                "selection_type": "directory",
                "title": {
                    "id": "",
                    "text": "Choose Folder",
                    "translatable": True
                },
                "tooltip": {
                    "id": "",
                    "text": "Click to select a folder",
                    "translatable": True
                },
                "type": "input::file"
            }
        ]
    ],
    "control": {
        "id": "OkCancel"
    },
    "embedding": "",
    "position": "",
    "size": {
        "height": 112,
        "width": 271
    },
    "sizemode": "",
    "style": "Standard",
    "title": {
        "id": "",
        "text": "List files in a folder",
        "translatable": True
    }
})

dir = RESULT.directory
print('Files in directory', dir + ':')
for filename in os.listdir(dir):
    print('  File:', filename)
