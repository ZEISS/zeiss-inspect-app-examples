# -*- coding: utf-8 -*-
#
# text_extraction.py
#
# Convert measurement to PNG image, display image and perform text detection
# This is the second stage of the TextDetection implementation
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import pytesseract
import cv2
import numpy as np

#
# Path to the installed terresact executable
#
TESSERACT_PATH = '<ENTER PATH TO TESSERACT BINARY HERE>'

def get_image ():
    '''
    Get RGB image data from measurement
    '''
    measurement = gom.app.project.measurement_series['Scan 1'].measurements['M1']
    acquisition = gom.api.project.get_image_acquisition (measurement, 'left camera',[0])[0]

    image = np.array (measurement.images['left camera'].data.rgb )[0]
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def get_preview_image ():
    '''
    Get a preview image of the measurement from left camera
    '''
    measurement = gom.app.project.measurement_series['Scan 1'].measurements['M1']
    acquisition = gom.api.project.get_image_acquisition (measurement, 'left camera',[0])[0]

    image = np.array (measurement.images['left camera'].data.rgb )[0]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return cv2.resize (image, (640, 480))

def image_to_png (image):
    '''
    Convert image to PNG 
    '''
    _, data = cv2.imencode(".png", image)
    return data.tobytes()

image = get_image ()

def detect_text (threshold):
    '''
    Perform text detection
    '''
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    results = pytesseract.image_to_data (image,
                                         output_type=pytesseract.Output.DICT,
                                         config='--oem 3 --psm 1')

    result = []
    for text, confidence in zip (results['text'], results['conf']):
        if confidence > threshold and len (text) > 0:
            result.append (text)

    return ' '.join (result)

DIALOG=gom.script.sys.create_user_defined_dialog (file='text_extraction.gdlg')

def dialog_handler (object):
    '''
    Dialog handler
    '''
    if object == DIALOG.detect:
        DIALOG.threshold.enabled = False
        DIALOG.detect.enabled = False

        text = detect_text (DIALOG.threshold.value)
        if text:
            DIALOG.text.text = text
        else:
            DIALOG.text.text = '-'

        DIALOG.threshold.enabled = True
        DIALOG.detect.enabled = True

DIALOG.image.data = image_to_png (cv2.resize (image, (640, 480)))

DIALOG.handler = dialog_handler

gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
