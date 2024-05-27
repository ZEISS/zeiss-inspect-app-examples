#!/usr/bin/python
#
# settings.py - Example for saving and restoring settings permanently
#               in the application preferences
#

import gom

DIALOG = gom.script.sys.create_user_defined_dialog(dialog={
    "content": [
        [
            {
                "columns": 1,
                "name": "text_label",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "Text",
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
                "name": "text",
                "password": False,
                "read_only": False,
                "rows": 1,
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "input::string",
                        "value": ""
            }
        ],
        [
            {
                "columns": 2,
                "maximum_size": -1,
                "minimum_size": 0,
                "name": "spacer",
                "rows": 1,
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "spacer::horizontal"
            },
            {
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
        "width": 351
    },
    "sizemode": "automatic",
    "style": "",
    "title": {
        "id": "",
                "text": "Size remembering dialog",
                "translatable": True
    }
})

DIALOG.width = gom.api.settings.get('dialog.size.width')
DIALOG.height = gom.api.settings.get('dialog.size.height')
DIALOG.text.value = gom.api.settings.get('dialog.magic')

gom.script.sys.show_user_defined_dialog(dialog=DIALOG)

gom.api.settings.set('dialog.size.width', DIALOG.width)
gom.api.settings.set('dialog.size.height', DIALOG.height)
gom.api.settings.set('dialog.magic', DIALOG.text.value)
