# -*- coding: utf-8 -*-
#
# ScrActVolume.py
#
# Example for creating a scripted volume element from artificial voxel data (Numpy Array)
#
# NOTE: This example requires ZEISS INSPECT X-Ray
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import math
from math import sin, cos
import numpy as np
import random


def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='scr_act_volume.gdlg')

    if 'gv_background' in params:
        DIALOG.gv_background.value = params['gv_background']
    if 'gv_mat1' in params:
        DIALOG.gv_mat1.value = params['gv_mat1']
    if 'gv_mat2' in params:
        DIALOG.gv_mat2.value = params['gv_mat2']
    if 'dx' in params:
        DIALOG.dx.value = params['dx']
    if 'dy' in params:
        DIALOG.dy.value = params['dy']
    if 'dz' in params:
        DIALOG.dz.value = params['dz']
    if 'rx' in params:
        DIALOG.rx.value = params['rx']
    if 'ry' in params:
        DIALOG.ry.value = params['ry']
    if 'rz' in params:
        DIALOG.rz.value = params['rz']

    # Get previous element name, when started from "Edit creation"
    if len(params) > 0:
        DIALOG.name.value = context.name

    # -------------------------------------------------------------------------
    def dialog_event_handler(widget):
        # No treatment of system events
        if str(widget) == 'system':
            return
        # If preview calculation returned with error
        if str(widget) == 'error':
            DIALOG.control.status = context.error
            return
        # If preview calculation was successful
        if str(widget) == 'calculated':
            DIALOG.control.status = ''
            DIALOG.control.ok.enabled = True
            return
        if widget == DIALOG.random:
            if DIALOG.random.value == True:
                DIALOG.rx.enabled = False
                DIALOG.ry.enabled = False
                DIALOG.rz.enabled = False
                DIALOG.rx.value = random.randrange(0, 3) * math.pi / 2
                DIALOG.ry.value = random.randrange(0, 3) * math.pi / 2
                DIALOG.rz.value = random.randrange(0, 3) * math.pi / 2
            else:
                DIALOG.rx.enabled = True
                DIALOG.ry.enabled = True
                DIALOG.rz.enabled = True

        # All other changes in the dialog --> calculate preview
        params['gv_background'] = DIALOG.gv_background.value
        params['gv_mat1'] = DIALOG.gv_mat1.value
        params['gv_mat2'] = DIALOG.gv_mat2.value
        params['dx'] = DIALOG.dx.value
        params['dy'] = DIALOG.dy.value
        params['dz'] = DIALOG.dz.value
        params['rx'] = DIALOG.rx.value
        params['ry'] = DIALOG.ry.value
        params['rz'] = DIALOG.rz.value

        context.name = DIALOG.name.value
        DIALOG.control.ok.enabled = False
        context.calc(params=params, dialog=DIALOG)

    DIALOG.handler = dialog_event_handler
    # -------------------------------------------------------------------------
    gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    return params


def set_voxeldata(voxels, gv, e):
    """Set the gray value of some voxels

    :param voxels: np.array() of shape (70, 70, 70)
:param gv: gray value to set
    :param e: extend around (fixed) nominal voxel coordinate
    """

    # (1) - front
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[35 + x, e + y, 35 + z] = gv

    # (6) - back
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[15 + x, 69 - e + y, 15 + z] = gv
                voxels[15 + x, 69 - e + y, 35 + z] = gv
                voxels[15 + x, 69 - e + y, 55 + z] = gv
                voxels[55 + x, 69 - e + y, 15 + z] = gv
                voxels[55 + x, 69 - e + y, 35 + z] = gv
                voxels[55 + x, 69 - e + y, 55 + z] = gv

    # (3) - top
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[15 + x, 15 + y, 69 - e + z] = gv
                voxels[35 + x, 35 + y, 69 - e + z] = gv
                voxels[55 + x, 55 + y, 69 - e + z] = gv

    # (4) - bottom
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[15 + x, 15 + y, e + z] = gv
                voxels[15 + x, 55 + y, e + z] = gv
                voxels[55 + x, 55 + y, e + z] = gv
                voxels[55 + x, 15 + y, e + z] = gv

    # (2) - left
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[x, 15 + y, 15 + z] = gv
                voxels[x, 55 + y, 55 + z] = gv

    # (5) - right
    for x in range(-e, e + 1):
        for y in range(-e, e + 1):
            for z in range(-e, e + 1):
                voxels[69 - e + x, 15 + y, 15 + z] = gv
                voxels[69 - e + x, 15 + y, 55 + z] = gv
                voxels[69 - e + x, 55 + y, 55 + z] = gv
                voxels[69 - e + x, 55 + y, 15 + z] = gv
                voxels[69 - e + x, 35 + y, 35 + z] = gv


# -------------------------------------------------------------------------
def calculation(context, params):
    valid_results = False

    e = 4
    gv0 = params['gv_background']
    gv1 = params['gv_mat1']
    gv2 = params['gv_mat2']
    voxels = np.ones((70, 70, 70), dtype=np.uint16)
    voxels = voxels * gv1
    set_voxeldata(voxels, gv2, e)
    voxels = np.pad(voxels, 30, 'constant', constant_values=gv0)

    rx = params['rx']
    ry = params['ry']
    rz = params['rz']
    dx = params['dx']
    dy = params['dy']
    dz = params['dz']

    transformation = gom.Mat4x4([
        cos(rz) * cos(ry), cos(rz) * sin(ry) * sin(rx) - sin(rz) *
        cos(rx), cos(rz) * sin(ry) * cos(rx) + sin(rz) * sin(rx), dx - 35,
        sin(rz) * cos(ry), sin(rz) * sin(ry) * sin(rx) + cos(rz) *
        cos(rx), sin(rz) * sin(ry) * sin(rx) - cos(rz) * sin(rx), dy - 35,
        -sin(ry), cos(ry) * sin(rx), cos(ry) * cos(rx), dz - 35,
        0, 0, 0, 1
    ])

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {'voxel_data': voxels, 'transformation': transformation}
            context.data[stage] = {"ude_mykey": "Scripted Volume"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
