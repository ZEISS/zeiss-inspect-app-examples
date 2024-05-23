# -*- coding: utf-8 -*-

import gom
import cv2
import numpy as np

#
# Read image from project
#
def get_image ():

	#
	# It is assumed that the measurement series 'Scan 1' contains images
	#
	measurement = gom.app.project.measurement_series['Scan 1'].measurements[0]
	image = np.array (measurement.images['left camera'].data.rgb )[0]
	return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	
def image_to_png (image):
	_, data = cv2.imencode(".png", image)
	return data.tobytes()

image = get_image ()

DIALOG=gom.script.sys.create_user_defined_dialog (file='dialog.gdlg')

DIALOG.image.data = image_to_png (cv2.resize (image, (640, 480)))

gom.script.sys.show_user_defined_dialog (dialog=DIALOG)


