# -*- coding: utf-8 -*-
#
# LocationScalarElement.py
#
# Location data from
# * Manual input,
# * Element keywords or
# * Project keywords
# is passed to the OSMMapDiagram service
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom

# -------------------------------------------------------------------------


def dialog(context, params):

    DIALOG=gom.script.sys.create_user_defined_dialog (dialog={
    "content": [
        [
            {
                "columns": 1,
                "name": "label_8",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "Name",
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
                "basename": {
                    "id": "",
                    "text": "GeoLocation",
                    "translatable": True
                },
                "columns": 2,
                "mode": "manually",
                "name": "name",
                "numbering": True,
                "read_only": False,
                "rows": 1,
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "input::elementname"
            },
            {
            }
        ],
        [
            {
                "columns": 3,
                "name": "separator_1",
                "rows": 1,
                "title": {
                    "id": "",
                    "text": "Geolocation parameters",
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
            },
            {
            }
        ],
        [
            {
                "columns": 1,
                "name": "label_0",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "Location source",
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
                "columns": 2,
                "default": "Manual",
                "items": [
                    {
                        "id": "",
                        "text": "Manual",
                        "translatable": True
                    },
                    {
                        "id": "",
                        "text": "Project",
                        "translatable": True
                    },
                    {
                        "id": "",
                        "text": "Element",
                        "translatable": True
                    }
                ],
                "name": "source",
                "rows": 1,
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "input::list"
            },
            {
            }
        ],
        [
            {
                "columns": 1,
                "name": "label_7",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "Element",
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
                "columns": 2,
                "fast_filter": False,
                "name": "element",
                "rows": 1,
                "supplier": "custom",
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "input::point3d"
            },
            {
            }
        ],
        [
            {
                "columns": 1,
                "name": "label_6",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "Label (optional)",
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
                "columns": 2,
                "name": "label",
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
            },
            {
            }
        ],
        [
            {
                "columns": 1,
                "name": "label_3",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "Latitude [°]",
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
                "background_style": "",
                "columns": 2,
                "default_precision": False,
                "maximum": 90,
                "minimum": -90,
                "name": "lat",
                "precision": 7,
                "rows": 1,
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "input::number",
                "unit": "",
                "value": 0
            },
            {
            }
        ],
        [
            {
                "columns": 1,
                "name": "label_4",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "Longitude [°]",
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
                "background_style": "",
                "columns": 2,
                "default_precision": False,
                "maximum": 180,
                "minimum": -180,
                "name": "lon",
                "precision": 7,
                "rows": 1,
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "input::number",
                "unit": "",
                "value": 0
            },
            {
            }
        ],
        [
            {
                "columns": 1,
                "name": "label_5",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "Altitude",
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
                "name": "en_alt",
                "rows": 1,
                "title": {
                    "id": "",
                    "text": "Enable",
                    "translatable": True
                },
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "input::checkbox",
                "value": False
            },
            {
                "background_style": "",
                "columns": 1,
                "default_precision": True,
                "maximum": 10000,
                "minimum": -10000,
                "name": "alt",
                "precision": 2,
                "rows": 1,
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "input::number",
                "unit": "",
                "value": 0
            }
        ],
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
                "columns": 2,
                "name": "label_1",
                "rows": 1,
                "text": {
                    "id": "",
                    "text": "See Preferences ► App-Settings for map configuration",
                    "translatable": True
                },
                "tooltip": {
                    "id": "",
                    "text": "",
                    "translatable": True
                },
                "type": "label",
                "word_wrap": True
            },
            {
            }
        ]
    ],
    "control": {
        "id": "OkCancel"
    },
    "embedding": "always_toplevel",
    "position": "automatic",
    "size": {
        "height": 445,
        "width": 334
    },
    "sizemode": "automatic",
    "style": "",
    "title": {
        "id": "",
        "text": "Geolocation parameters",
        "translatable": True
    }
})

    # Restore dialog widgets from parameters
    if 'source' in params:
        DIALOG.source.value = params['source']
    if 'label' in params:
        DIALOG.label.value = params['label']
    if 'element' in params:
        DIALOG.element.value = params['element']
    if 'lat' in params:
        DIALOG.lat.value = params['lat']
    if 'lon' in params:
        DIALOG.lon.value = params['lon']
    if 'en_alt' in params:
        DIALOG.en_alt.value = params['en_alt']
    if 'alt' in params:
        DIALOG.alt.value = params['alt']

    # Get previous element name, when started from "Edit creation"
    if len(params) > 0:
        DIALOG.name.value = context.name

    # -------------------------------------------------------------------------
    def dialog_event_handler(widget):
        # If preview calculation returned with error
        if str(widget) == 'error':
            DIALOG.control.status = context.error
            print("Error")
            return

        if str(widget) == 'initialize' or widget == DIALOG.source:

            # Location info from project keywords
            if DIALOG.source.value == 'Project':
                try:
                    print(gom.app.project.project_keywords)
                    if 'user_GPSLatitude' in gom.app.project.project_keywords:
                        DIALOG.lat.value = gom.app.project.get('user_GPSLatitude')
                    if 'user_GPSLongitude' in gom.app.project.project_keywords:
                        DIALOG.lon.value = gom.app.project.get('user_GPSLongitude')
                    if 'user_GPSAltitude' in gom.app.project.project_keywords:
                        DIALOG.alt.value = gom.app.project.get('user_GPSAltitude')
                except:
                    DIALOG.lat.value = 0.0
                    DIALOG.lon.value = 0.0
                    DIALOG.alt.value = 0.0
                DIALOG.element.enabled = False
                DIALOG.lat.enabled = False
                DIALOG.lon.enabled = False
                DIALOG.alt.enabled = False

            # Location info from element keywords
            # CAUTION:
            # If an element keyword does not exist, the project keyword is propagated
            # as element keyword!
            elif DIALOG.source.value == 'Element':
                try:
                    #print(DIALOG.element.value.element_keywords)
                    if 'user_GPSLatitude' in DIALOG.element.value.element_keywords:
                        DIALOG.lat.value = DIALOG.element.value.user_GPSLatitude
                    if 'user_GPSLongitude' in DIALOG.element.value.element_keywords:
                        DIALOG.lon.value = DIALOG.element.value.user_GPSLongitude
                    if 'user_GPSAltitude' in DIALOG.element.value.element_keywords:
                        DIALOG.alt.value = DIALOG.element.value.user_GPSAltitude
                except:
                    DIALOG.lat.value = 0.0
                    DIALOG.lon.value = 0.0
                    DIALOG.alt.value = 0.0
                DIALOG.element.enabled = True
                DIALOG.lat.enabled = False
                DIALOG.lon.enabled = False
                DIALOG.alt.enabled = False
            else:
                # 'Manual'
                DIALOG.element.enabled = False
                DIALOG.lat.enabled = True
                DIALOG.lon.enabled = True
                DIALOG.alt.enabled = True

        # Select element as source for location info
        if widget == DIALOG.element:
            try:
                #print(DIALOG.element.value.element_keywords)
                if 'user_GPSLatitude' in DIALOG.element.value.element_keywords:
                    DIALOG.lat.value = DIALOG.element.value.user_GPSLatitude
                if 'user_GPSLongitude' in DIALOG.element.value.element_keywords:
                    DIALOG.lon.value = DIALOG.element.value.user_GPSLongitude
                if 'user_GPSAltitude' in DIALOG.element.value.element_keywords:
                    DIALOG.alt.value = DIALOG.element.value.user_GPSAltitude
            except:
                DIALOG.lat.value = 0.0
                DIALOG.lon.value = 0.0
                DIALOG.alt.value = 0.0

        # If preview calculation was successful
        if str(widget) == 'calculated':
            DIALOG.control.status = ''
            DIALOG.control.ok.enabled = True
            return

        # Assign calculation parameters
        params['name'] = DIALOG.name.value
        params['source'] = DIALOG.source.value
        params['label'] = DIALOG.label.value
        params['element'] = DIALOG.element.value
        params['lat'] = DIALOG.lat.value
        params['lon'] = DIALOG.lon.value
        params['en_alt'] = DIALOG.en_alt.value
        params['alt'] = DIALOG.alt.value

    context.name = DIALOG.name.value
    DIALOG.element.filter = lambda elem: not getattr(elem, "user_GPSLongitude", None) is None and not getattr(elem, "user_GPSLatitude", None) is None
    DIALOG.handler = dialog_event_handler
    gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    return params
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------


def calculation(context, params):
    valid_results = False

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = 42 # Unused
            context.data[stage] = {
                "ude_diagram_custom": 1,
                "ude_diagram_type": "SVGDiagram",
                "ude_diagram_service" : "gom.api.osm.geolocation",
                "ude_diagram_name": params['name'],
                "ude_diagram_lat": params['lat'],
                "ude_diagram_lon": params['lon'],
                "ude_diagram_alt": params['alt'],
                "ude_diagram_alt_en": params['en_alt'],
                "ude_diagram_label": params['label']
            }
            print(f'{context.data[stage]}')
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True

    return valid_results

# -------------------------------------------------------------------------
