# -*- coding: utf-8 -*-
#
# TestServerApp.py
#
# ZEISS INSPECT Inter Process Communication (IPC) via Internet Sockets Example
#
# Socket Server App
# 
# The server is listening on host <HOST> port <PORT> for requests.
# 
# The following requests are implemented:
# 1. {"image": {"file": <image_file path>, "name": <measurement_series>, "focal_length": <focal_length_in_mm>}}
#    If the requested measurement series does not exist yet, it is created with the command 
#    gom.script.sys.create_measurement_series_for_other_images().
#    Then, the image is imported with the command gom.script.sys.import_other_images().
#
# 2. {"elements": {"file": <elements_file_path>, "import_mode": <import_mode>}}
#    where <import_mode>: "clipboard" or "new_stage"
#    The elements are imported with the command gom.script.sys.import_gom_inspection_exchange().
#
# 3. quit
#    Close the connection and terminate the App.
#
# For each request, a response is sent as plain text.

#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This test is part of the "Python API Examples" Add-on.
# https://zeissiqs.github.io/zeiss-inspect-addon-api/main/python_examples/
# ---

import gom
import json
import os
import asyncio

from websockets.asyncio.server import serve

HOST = 'localhost'
PORT = 40010

def waitForClosing():
	RESULT=gom.script.sys.execute_user_defined_dialog (file='TestServerClose.gdlg')
	print("Window closed")

def decodeMessage(message):
	response = "O.k."
	if 'image' in message:
		if not 'file' in message['image']:
			return "Error: Missing parameter 'file' in 'image' request."
		if not 'name' in message['image']:
			return "Error: Missing parameter 'name' in 'image' request."
		if not 'focal_length' in message['image']:
			return "Error: Missing parameter 'focal_length' in 'image' request."
			
		file = message['image']['file']
		name = message['image']['name']
		focal_length = message['image']['focal_length']
		
		if not os.path.isfile(file) or not os.access(file, os.R_OK):
			return f"Error: Image file {file} could not be read."
		
		try:
			gom.app.project.measurement_series[name]
		except gom.RequestError:
			gom.script.sys.create_measurement_series_for_other_images (
				camera_focal_length=focal_length, 
				name=name
			)			
		
		try:
			# GOM Command
			print(f"Loading image from {file} as '{name}' with focal_length {focal_length}")
			gom.script.sys.import_other_images (
				image_files=[gom.File (file)], 
				measurement_series=gom.app.project.measurement_series[name]
            )
		except:
			return f"Error: Image could not be imported from file {file}."
		
	elif 'elements' in message:
		if not 'file' in message['elements']:
			return "Error: Missing parameter 'file' in 'elements' request."
			
		if not 'import_mode' in message['elements']:
			return "Error: Missing parameter 'import_mode' in 'elements' request."
		
		file = message['elements']['file']
		import_mode = message['elements']['import_mode']
		
		if not os.path.isfile(file) or not os.access(file, os.R_OK):
			return f"Error: Elements file {file} could not be read."
		
		try:
			# GOM Command
			print(f"Importing elements from {file} with import mode '{import_mode}'")
			gom.script.sys.import_gom_inspection_exchange (
				files=[file], 
				import_mode=import_mode
			)
		except:
			return f"Error: Elements could not be imported from file {file} with import mode {import_mode}."
	
	elif 'quit' in message:
		return "bye"
	
	else:
		return f"Error: Unknown request:\n{message}"
	
	return "O.k."

DIALOG=gom.script.sys.create_user_defined_dialog (file='TestServerApp.gdlg')

#
# Event handler function
#
def dialog_event_handler (widget):
	"""Initialize continuous text widget with HTML string containing variables
	
	Args:
		widget:	widget event
	"""
	if str(widget) == 'initialize':
		DIALOG.text.text = f'<html><p><span style="font-weight:600;">ZEISS INSPECT Socket Server</span></p><p style="-qt-paragraph-type:empty;\
       font-weight:600;"><br/></p><p>Server will be started on <b>{HOST}</b> waiting for client connections on <b>port {PORT}</b>.<br/> \
       Press <b>Esc</b> in the ZEISS INSPECT main window or close the client window to terminate.</p><p style="-qt-paragraph-type:empty;"><br/></p>\
       <p style="-qt-paragraph-type:empty;"><br/></p></html>'

DIALOG.handler = dialog_event_handler

gom.script.sys.show_user_defined_dialog (dialog=DIALOG)

async def server(websocket):
	async for request in websocket:
		print(f"{request=}")
		
		if request.startswith("quit"):
			await websocket.send("bye")
			await websocket.close(code=1000, reason="Closing connection.")
			print("Connection closed by client.")
			sys.exit(0)
			
		try:
			message = json.loads(request)
			print(message)
		except json.JSONDecodeError:
			response = "Error: Malformed JSON message."
		else:
			"""Decode JSON message"""
			response = decodeMessage(message)

		try:
			await websocket.send(response)
		except websockets.exceptions.ConnectionClosed:
			print("Connection closed by the client.")
			break
	
	await websocket.close(code=1000, reason="Closing connection.")

async def main():
	async with serve(server, HOST, PORT):
		await asyncio.get_running_loop().create_future()
		sys.exit(0)

if __name__ == "__main__":
	asyncio.run(main())
