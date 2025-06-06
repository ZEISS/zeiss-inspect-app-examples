#
# step2.py - Sample script for workspace
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---
"""Sample script for workspace"""

import gom

RESULT = gom.script.sys.execute_user_defined_dialog(dialog={
    "content": [
        [
            {
                "columns": 1,
                "name": "text",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "Step 2",
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
        "id": "OkCancel"
    },
    "embedding": "always_toplevel",
    "position": "automatic",
    "size": {
        "height": 108,
        "width": 210
    },
    "sizemode": "automatic",
    "style": "",
    "title": {
        "id": "",
                "text": "Message",
                "translatable": True
    }
})
