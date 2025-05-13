# -*- coding: utf-8 -*-
#
# ScrActVolumeRegion.py
#
# Example for creating a scripted volume region element from artificial voxel data (Numpy Array)
#
# The offset of the element in the coordinate system and the shape of the voxel data are
# provided as parameters.
#
# NOTE: This example requires ZEISS INSPECT X-Ray
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import numpy as np


def dialog(context, params):
  DIALOG = gom.script.sys.create_user_defined_dialog(file='scr_act_volume_region.gdlg')

  if 'x0' in params:
    DIALOG.x0.value = params['x0']
  if 'y0' in params:
    DIALOG.y0.value = params['y0']
  if 'z0' in params:
    DIALOG.z0.value = params['z0']

  if 'dx' in params:
    DIALOG.dx.value = params['dx']
  if 'dy' in params:
    DIALOG.dy.value = params['dy']
  if 'dz' in params:
    DIALOG.dz.value = params['dz']

  if 'volume_ele' in params:
    DIALOG.volume_ele.value = params['volume_ele']

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

    # All other changes in the dialog --> calculate preview
    params['x0'] = DIALOG.x0.value
    params['y0'] = DIALOG.y0.value
    params['z0'] = DIALOG.z0.value
    params['dx'] = DIALOG.dx.value
    params['dy'] = DIALOG.dy.value
    params['dz'] = DIALOG.dz.value
    params['volume_ele'] = DIALOG.volume_ele.value

    if DIALOG.volume_ele.value is not None:
      context.name = str(DIALOG.volume_ele.value) + ".Region"

    DIALOG.control.ok.enabled = False
    context.calc(params=params, dialog=DIALOG)

  def element_filter(element):
    try:
      if element.type == 'volume' or element.type == 'linked_volume':
        return True
    except Exception as e:
      pass
    return False

  DIALOG.volume_ele.filter = element_filter
  DIALOG.handler = dialog_event_handler
  # -------------------------------------------------------------------------
  RESULT = gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
  return params

# -------------------------------------------------------------------------
def calculation(context, params):
  valid_results = False

  if params['volume_ele'] == None:
    context.error[context.stages[0]] = 'No volume selected.'
    return False

  x0 = params['x0']
  y0 = params['y0']
  z0 = params['z0']

  dx = int(params['dx'] / params['volume_ele'].voxel_size.x)
  dy = int(params['dy'] / params['volume_ele'].voxel_size.y)
  dz = int(params['dz'] / params['volume_ele'].voxel_size.z)

  # Calculating all available stages
  for stage in context.stages:
    # Access element properties with error handling
    try:
      context.result[stage] = {
        'volume_element': params['volume_ele'],
        'offset': gom.Vec3d(x0, y0, z0),
        'voxel_data': np.ones((dx, dy, dz), dtype=np.uint8)
      }
      context.data[stage] = {"ude_mykey": "Scripted Volume Region"}
    except Exception as error:
      context.error[stage] = str(error)
    else:
      valid_results = True
  return valid_results
# -------------------------------------------------------------------------
