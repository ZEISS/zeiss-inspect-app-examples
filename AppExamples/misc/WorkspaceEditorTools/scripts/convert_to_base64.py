#
# convert_to_base64.py - Convert a file into base64 format
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---
"""Convert a file into base64 format"""
import gom
import base64
import os

RESULT = gom.script.sys.execute_user_defined_dialog(dialog={
    "content": [
        [
            {
                "columns": 2,
                "default_font_family": "",
                "default_font_size": 0,
                "name": "description",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "<html><p> This tool will create a file named &lt;yourfilename>.b64 in the same directory as the source file containing the base 64 encoded data from that source file.</p></html>",
                    "translatable": True
                },
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "display::text",
                "wordwrap": True
            },
            {
            }
        ],
        [
            {
                "columns": 1,
                "name": "file_label",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "File",
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
                "default": "",
                "file_types": [
                ],
                "file_types_default": "",
                "limited": False,
                "name": "file",
                "rows": 1,
                "selection_type": "file",
                "title": {
                    "id": "",
                    "text": "Choose file to be encoded",
                    "translatable": True
                },
                "tooltip": {
                    "id": "",
                    "text": "",
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
    "position": "automatic",
    "size": {
        "height": 224,
        "width": 422
    },
    "sizemode": "fixed",
    "style": "",
    "title": {
        "id": "",
        "text": "Convert to base 64",
        "translatable": True
    }
})

with open(RESULT.file, 'rb') as f:
    data = base64.b64encode(f.read())

target = os.path.splitext(RESULT.file)[0] + '.b64'
with open(target, 'w', encoding='utf-8') as f:
    f.write(data.decode('utf-8'))

gom.script.sys.execute_user_defined_dialog(dialog={
    "content": [
        [
            {
                "columns": 1,
                "data": "AAAAAA==",
                "file_name": "",
                "height": 0,
                "keep_aspect": True,
                "keep_original_size": True,
                "name": "image",
                "rows": 1,
                "system_image": "system_message_information",
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "image",
                "use_system_image": True,
                "width": 0
            },
            {
                "columns": 1,
                "default_font_family": "",
                "default_font_size": 0,
                "name": "text",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": f"'{target}' has been generated",
                    "translatable": True
                },
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "display::text",
                "wordwrap": False
            }
        ]
    ],
    "control": {
        "id": "Close"
    },
    "embedding": "always_toplevel",
    "position": "automatic",
    "size": {
        "height": 184,
        "width": 437
    },
    "sizemode": "automatic",
    "style": "",
    "title": {
        "id": "",
        "text": "Message",
        "translatable": True
    }
})
