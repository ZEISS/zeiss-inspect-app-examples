# -*- coding: utf-8 -*-
#
# walkdir_import_scripts.py
#
# Traverses a directory tree and imports all Python scripts
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
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
                    "text": "Klick to select a folder",
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
for (basepath, subfolders, filenames) in os.walk(dir):
    for filename in filenames:
        base, ext = os.path.splitext(filename)
        if ext == '.py':
            scriptfile = os.path.join(basepath, filename)
            basename, _ = os.path.splitext(filename)
            gom.script.sys.import_script (
                config_level='user',
                display_names=[basename],
                files=[scriptfile],
                names=['test.' + basename],
                replace_existing_scripts=True)
