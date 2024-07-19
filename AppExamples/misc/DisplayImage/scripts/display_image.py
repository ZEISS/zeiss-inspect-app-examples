# -*- coding: utf-8 -*-
#
# display_image.py
#
# Display an optical measurement using the image widget
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import cv2
import numpy as np

def get_image ():
    """ Read image from project """

    #
    # It is assumed that the measurement series 'Scan 1' contains images
    #
    measurement = gom.app.project.measurement_series['Scan 1'].measurements[0]
    image = np.array (measurement.images['left camera'].data.rgb )[0]
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def image_to_png (image):
    """ Convert image to PNG """

    _, data = cv2.imencode(".png", image)
    return data.tobytes()

image = get_image ()

DIALOG=gom.script.sys.create_user_defined_dialog (file='dialog.gdlg')

DIALOG.image.data = image_to_png (cv2.resize (image, (640, 480)))

gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
