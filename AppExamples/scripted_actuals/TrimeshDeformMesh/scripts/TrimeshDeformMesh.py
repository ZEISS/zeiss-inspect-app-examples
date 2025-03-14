# -*- coding: utf-8 -*-
#
# trimesh_deform_mesh.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

# NOTE: Open a project with a mesh, e.g. "zeiss_part_test_project" from the examples
# to try this example properly.

import gom
import numpy as np
import trimesh

#
# This function will show the creation / editing dialog
#


def dialog(context, params):

    DIALOG = gom.script.sys.create_user_defined_dialog(dialog={
        "content": [
            [
                {
                    "columns": 1,
                    "name": "label_1",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": "Mesh to deform:",
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
            ],
            [
                {
                    "columns": 1,
                    "fast_filter": False,
                    "name": "selected_element",
                    "rows": 1,
                    "supplier": "custom",
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "input::point3d"
                }
            ],
            [
                {
                    "columns": 1,
                    "name": "label_2",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": "Deformed element name:",
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
            ],
            [
                {
                    "basename": {
                        "id": "",
                        "text": "Deformed Mesh",
                        "translatable": True
                    },
                    "columns": 1,
                    "mode": "manually",
                    "name": "elementname",
                    "numbering": True,
                    "read_only": False,
                    "rows": 1,
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "input::elementname"
                }
            ],
            [
                {
                    "columns": 1,
                    "name": "label",
                    "rows": 1,
                    "text": {
                        "id": "",
                        "text": "Deformation value:",
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
            ],
            [
                {
                    "background_style": "",
                    "columns": 1,
                    "maximum": 1000,
                    "minimum": 0,
                    "name": "deformation_value",
                    "precision": 2,
                    "rows": 1,
                    "tooltip": {
                        "id": "",
                        "text": "",
                        "translatable": True
                    },
                    "type": "input::number",
                    "unit": "",
                    "value": 0.2
                }
            ]
        ],
        "control": {
            "id": "OkCancel"
        },
        "embedding": "",
        "position": "",
        "size": {
            "height": 262,
            "width": 198
        },
        "sizemode": "",
        "style": "",
        "title": {
            "id": "",
            "text": "Trimesh Deform Mesh",
            "translatable": True
        }
    })

    #
    # SETUP EDIT CREATION
    #
    if context.is_new_element and len(params) > 0:
        DIALOG.elementname.value = context.name
    if 'selected_element' in params:
        DIALOG.selected_element.value = params['selected_element']
    if 'deformation_value' in params:
        DIALOG.deformation_value.value = params['deformation_value']

    #
    # SELECTION FILTER for element to deform
    # -------------------------------------------------------------------------
    def element_filter(element):
        try:
            if element.type in ['mesh', 'cad_body']:
                return True
        except Exception as e:
            pass
        return False

    DIALOG.selected_element.filter = element_filter
    # -------------------------------------------------------------------------

    gom.script.sys.show_user_defined_dialog(dialog=DIALOG)

    # NAME & PARAM setting
    context.name = DIALOG.elementname.value
    params['selected_element'] = DIALOG.selected_element.value
    params['deformation_value'] = DIALOG.deformation_value.value

    return params

#
# Calculation: deforming the selected mesh
#


def calculation(context, params):

    selected_element = params['selected_element']
    deformation = params['deformation_value']

    for s in context.stages:
        # -------------------------------------------------------------------------
        vertices = np.array(selected_element.data.coordinate)[s]
        triangles = np.array(selected_element.data.triangle)[s]

        # Creating a mesh in 3rd party library "trimesh"
        mesh = trimesh.Trimesh(vertices, triangles)

        # Using the deformation algorithm of trimesh
        deformed = trimesh.permutate.noise(mesh, deformation)

        # Converting to target dtypes
        deformed_vertices = deformed.vertices
        deformed_faces = np.array(deformed.faces, dtype=np.int32)

        # Setting the result to transfer back to the GOM Software
        context.result[s] = {'vertices': deformed_vertices, 'triangles': deformed_faces}
        # -------------------------------------------------------------------------
    return True
