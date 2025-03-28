# -*- coding: utf-8 -*-
#
# display_image.py
#
# Convert measurement to PNG image and display image in dialog
# This is the first stage of the TextDetection implementation
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import cv2
import numpy as np
from ExampleProjects.setup_project import open_project

def get_image ():
    '''
    Query image from project
    
    The image is read from a hardcoded measurement of the associated demo project for
    the sake of simplicity of this example.
    
    @return Image in RGB format as a numpy array of matching shape
    '''
    measurement = gom.app.project.measurement_series['Scan 1'].measurements['M1']

    image = np.array (measurement.images['left camera'].data.rgb )[0]
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def image_to_png (image):
    '''
    Convert image into PNG format
    
    @param image Image in numpy RGB format to be converted
    @return Image in PNG format
    '''
    _, data = cv2.imencode(".png", image)
    return data.tobytes()

if __name__ == '__main__':
    open_project('zeiss_training_object_42')

    # Define user defined dialog. The dialog is not displayed yet, but its widgets can be accessed
    DIALOG=gom.script.sys.create_user_defined_dialog (file='display_image.gdlg')

    # Display read, converted and rescaled image in the dialogs image viewing widget
    DIALOG.image.data = image_to_png (cv2.resize (get_image (), (1024, 768)))

    # Display user defined dialog. The script execution will be stalled here
    # until the dialog is closed again.
    gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
