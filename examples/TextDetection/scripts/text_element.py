# -*- coding: utf-8 -*-

import gom
import pytesseract
import cv2
import numpy as np

#
# Path to the installed terresact executable
#
TESSERACT_PATH = 'C:/Users/IQFBLANK/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

#
# Return left camera image of the given scan
#
def get_image (scan):
	image = np.array (scan.images['left camera'].data.rgb )[0]
	return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#
# Convert camera image into PNG format
#	
def image_to_png (image):
	_, data = cv2.imencode(".png", image)
	return data.tobytes()

#
# Detect text label in the given image
#
def detect_text (image, threshold):
	pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

	results = pytesseract.image_to_data (image, output_type=pytesseract.Output.DICT, config='--oem 3 --psm 1')
	
	result = []
	for text, confidence in zip (results['text'], results['conf']):
		if confidence > threshold and len (text) > 0:
			result.append (text)

	return ' '.join (result)

#
# Interactive (dialog handling) part of the scripted element
#
def dialog(context, params):

	DIALOG=gom.script.sys.create_user_defined_dialog (file='text_element.gdlg')
	
	#
	# Dialog handler function, called in case of dialog events
	#
	def dialog_handler (object):
		
		calc = False
		
		if object == 'initialize':
			image = get_image (DIALOG.element.value)
			DIALOG.image.data = image_to_png (cv2.resize (image, (640, 480)))
			
			calc = True
			
		elif object == 'calculated':
			DIALOG.result.text = '-'
			if 'ude_text' in context.data[0]:
				DIALOG.result.text = context.data[0]['ude_text']
		
		elif object == DIALOG.element:
			image = get_image (DIALOG.element.value)
			DIALOG.image.data = image_to_png (cv2.resize (image, (640, 480)))
			
			calc = True
			
		elif object == DIALOG.threshold:
			calc = True
			
		if calc:
			params['scan'] = DIALOG.element.value
			params['threshold'] = DIALOG.threshold.value
	
			context.name = 'Part id'
			DIALOG.control.ok.enabled = False
			
			result = context.calc (params=params, dialog=DIALOG)
			
			DIALOG.control.ok.enabled = True


	#
    # Filter for the elements which can be selected in the measurement selector
	#	
	def element_filter( element ):
		try:
			if element.type == 'scan':
				return True
		except Exception as e:
			pass
	
		return False
	
	DIALOG.element.filter = element_filter	
	DIALOG.handler = dialog_handler
	
	gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
	
	return params

#
# Calculation function for the scripted element
#	
def calculation(context, params):

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
	
