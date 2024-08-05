# -*- coding: utf-8 -*-
#
# TestServerApp.py
#
# ZEISS INSPECT Inter Process Communication (IPC) via Internet Sockets Example
#
# Socket Server App
# 
# The server is listening on host <HOST> port <PORT> for JSON requests terminated with <EOF>.
# For each request, a response is sent as plain text.
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import socket
import json
import os

HOST = 'localhost'
PORT = 7000
EOF = b'\x04' # Ctrl-D
ABORT = b'\x1A' # Ctrl-Z

# Telnet mode keeps the connection until shut down by the server.
TELNET_MODE = False

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
		
	else:
		return f"Error: Unknown request:\n{message}"
	
	return "O.k."

def is_internet_socket_open(sock):
	try:
		# Check if the socket is open
		if sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR) == 0:
			return True
		else:
			return False
	except socket.timeout:
		# Connection timed out
		return False
	except ConnectionRefusedError:
		# Connection refused
		return False
	except ConnectionAbortedError:
		return False
	except socket.error as err:
		# Other socket error
		if err.errno == socket.errno.ECONNRESET:
			# Connection reset by peer
			return False
		else:
			raise

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
       Press <b>Esc</b> in the ZEISS INSPECT main window to terminate.</p><p style="-qt-paragraph-type:empty;"><br/></p>\
       <p style="-qt-paragraph-type:empty;"><br/></p></html>'

DIALOG.handler = dialog_event_handler

gom.script.sys.show_user_defined_dialog (dialog=DIALOG)

			
while True:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		"""Wait for connection from client"""
		s.bind((HOST, PORT))
		s.listen()
		conn, addr = s.accept()
		with conn:
			print(f"Connected by {addr}")
			
			while is_internet_socket_open(conn):
				"""Receive request"""
				buffer = ""
				while True:
					data = conn.recv(1024)
					if not data or data == EOF:
						break
					if data == ABORT:
						print("Connection closed by peer.")
						conn.close()
						sys.exit(0)
					buffer += data.decode(encoding='utf-8')
					endPos =  buffer.find(EOF.decode('utf-8'))
					if endPos > -1:
						buffer = buffer[:endPos]
						break
				#print(buffer)
				
				try:
					message = json.loads(buffer)
					#print(message)
				except json.JSONDecodeError:
					response = "Error: Malformed JSON message.\r\n"
				else:
					"""Decode JSON message"""
					response = decodeMessage(message) + "\r\n"
					
				try:
					"""Send response"""
					conn.sendall(response.encode('utf-8'))
				except:
					pass
				
				if not TELNET_MODE:
					"""Close client connection after sending response."""
					conn.shutdown(socket.SHUT_WR)
					conn.close()
					break

