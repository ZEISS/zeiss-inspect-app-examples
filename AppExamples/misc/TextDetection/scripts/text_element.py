# -*- coding: utf-8 -*-
#
# text_element.py
#
# Convert measurement to PNG image, display image, perform text detection and
# create scripted element from test
# This is the third and final stage of the TextDetection implementation
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import os
import pytesseract
import cv2
import numpy as np
from ExampleProjects.setup_project import open_project


def get_image (scan):
    """Return left camera image of the given scan"""
    image = np.array (scan.images['left camera'].data.rgb )[0]
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def image_to_png (image):
    """Convert camera image into PNG format"""
    _, data = cv2.imencode(".png", image)
    return data.tobytes()


def detect_text (image, threshold):
    """Detect text label in the given image"""
    # Get path to installed terresact executable
    # 'C:/Users/<user>/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
    user_profile = os.environ.get('USERPROFILE')
    local_appdata_path = os.path.join(user_profile, 'AppData', 'Local')
    tesseract_path = os.path.join(local_appdata_path, 'Programs', 'Tesseract-OCR', 'tesseract.exe')

    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    results = pytesseract.image_to_data (image,
                                         output_type=pytesseract.Output.DICT,
                                         config='--oem 3 --psm 1'
                                        )

    result = []
    for text, confidence in zip (results['text'], results['conf']):
        if confidence > threshold and len (text) > 0:
            result.append (text)

    return ' '.join (result)


def dialog(context, params):
    """Interactive (dialog handling) part of the scripted element"""

    DIALOG=gom.script.sys.create_user_defined_dialog (file='text_element.gdlg')


    def dialog_handler (object):
        """Dialog handler function, called in case of dialog events"""

        calc = False

        if object == 'initialize' or object == DIALOG.element:
            image = get_image (DIALOG.element.value)
            DIALOG.image.data = image_to_png (cv2.resize (image, (640, 480)))

            calc = True

        elif object == 'calculated':
            DIALOG.result.text = '-'
            if 'ude_text' in context.data[0]:
                DIALOG.result.text = context.data[0]['ude_text']

        elif object == DIALOG.threshold:
            calc = True

        if calc:
            params['scan'] = DIALOG.element.value
            params['threshold'] = DIALOG.threshold.value

            context.name = 'Part id'
            DIALOG.control.ok.enabled = False

            context.calc (params=params, dialog=DIALOG)

            DIALOG.control.ok.enabled = True


    def element_filter( element ):
        """Filter for the elements which can be selected in the measurement selector"""
        try:
            if element.type == 'scan':
                return True
        except Exception:
            pass

        return False

    DIALOG.element.filter = element_filter    
    DIALOG.handler = dialog_handler

    gom.script.sys.show_user_defined_dialog (dialog=DIALOG)

    return params


def calculation(context, params):
    """Calculation function for the scripted element"""

    ok = False

    for stage in context.stages:
        try:
            scan = params['scan']
            threshold = params['threshold']

            image = get_image (scan)
            text = detect_text (image, threshold)

            ids = [float (s) for s in text.split () if s.isdigit ()]

            context.result[stage] = (ids[0] if len (ids) > 0 else -1)
            context.data[stage] = {'ude_text': text}

            ok = True

        except Exception as error:
            context.error[stage] = str (error)

    return ok

if __name__ == '__main__':
    open_project('zeiss_training_object_42')
