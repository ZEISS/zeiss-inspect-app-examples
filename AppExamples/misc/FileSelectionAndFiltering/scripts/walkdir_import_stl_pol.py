# -*- coding: utf-8 -*-
#
# walkdir_import_stl_pol.py
#
# Traverses a directory tree and and imports all `.pol` and `.stl` files
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
        if ext == '.stl':
            stlfile = os.path.join(basepath, filename)
            gom.script.sys.import_stl (
                bgr_coding=True,
                files=[stlfile],
                import_mode='new_elements',
                length_unit='mm',
                stl_color_bit_set=False,
                target_type='mesh')
        if ext == '.pol':
            polfile = os.path.join(basepath, filename)
            gom.script.sys.import_pol (
                files=[polfile], 
                import_mode='new_elements')
