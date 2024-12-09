# -*- coding: utf-8 -*-
#
# TestClientStandalone.py
#
# ZEISS INSPECT Inter Process Communication (IPC) via Internet Sockets Example
#
# Socket Client
#
# Standalone Python script with PySide6 GUI
# 
# Pressing a request button triggers a connection to the server <HOST> on port <PORT>,
# transmission of the request and reception of the response.
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This test is part of the "Python API Examples" Add-on.
# https://zeissiqs.github.io/zeiss-inspect-addon-api/main/python_examples/
# ---

import socket
import time
import asyncio

from websockets.asyncio.client import connect
from PySide6.QtCore import Qt, QSettings, QCoreApplication
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QSpacerItem, \
								QLabel, QFileDialog, QDoubleSpinBox, QComboBox, QLineEdit, QPushButton, QTextEdit

HOST = 'localhost'
"""string: Hostname or IP address"""

PORT = 40010
"""int: TCP/IP port"""

URI = f"ws://{HOST}:{PORT}"

EOF = b'\x04' # Ctrl-D
"""byte: End-of-file/Ctrl-D indicates end-of-request""" 

APP = "TestClient"
"""string: App name for settings storage"""

class MyWindow(QWidget):
	"""
	The MyWindow class allows to save the current widget settings when the program is closed
	and to restore them at startup
	"""
	def __init__(self):
		super().__init__()
		
		# Set the organization name and application name
		QCoreApplication.setOrganizationName("ZEISS")
		QCoreApplication.setApplicationName("ZEISS INSPECT IPC Test Client")
		# Load the widget settings
		self.loadSettings()
	
	def closeEvent(self, event):
		"""Quit the websocket connection and save the widget settings before closing
		
		Args:
			event: Qt event
		"""
		asyncio.run(transmitReceive("quit"))
		self.saveSettings()
		super().closeEvent(event)
		
	def loadSettings(self):
		"""Load the widget settings from the storage"""
		settings = QSettings()
		imageFilePathEdit.setText(settings.value(f"{APP}/ImageFile", ""))
		focalLengthSpinBox.setValue(
			focalLengthSpinBox.valueFromText(
				settings.value(f"{APP}/FocalLength",
					focalLengthSpinBox.textFromValue(focalLengthSpinBox.value())
				)
			)
		)
		measSeriesInput.setText(settings.value(f"{APP}/MeasurementSeries", ""))
		elementsFilePathEdit.setText(settings.value(f"{APP}/ElementsFile", ""))
		importModeComboBox.setCurrentIndex(settings.value(f"{APP}/ImportMode", 0))
	
	def saveSettings(self):
		"""Save the widget settings to the storage"""
		settings = QSettings()
		settings.setValue(f"{APP}/ImageFile", imageFilePathEdit.text())
		settings.setValue(f"{APP}/MeasurementSeries", measSeriesInput.text())
		settings.setValue(f"{APP}/FocalLength", focalLengthSpinBox.textFromValue(focalLengthSpinBox.value()))
		settings.setValue(f"{APP}/ElementsFile", elementsFilePathEdit.text())
		settings.setValue(f"{APP}/ImportMode", importModeComboBox.currentIndex())

def openImageFileDialog():
	"""Image file dialog"""
	fileDialog = QFileDialog()
	fileDialog.setNameFilter("JPEG files (*.jpeg *.jpg);;TIFF files (*.tif *.tiff);;All files (*.*)")
	if fileDialog.exec() == QFileDialog.Accepted:
		selectedFile = fileDialog.selectedFiles()[0]
		imageFilePathEdit.setText(selectedFile)
	checkImageFilePath()

def checkImageFilePath():
	"""Check if image file path is empty and enable/disable transmit button accordingly"""
	if imageFilePathEdit.text() == "":
		imageRequestButton.setEnabled(False)
	else:
		imageRequestButton.setEnabled(True)

def openElementsFileDialog():
	"""Elements file dialog"""
	fileDialog = QFileDialog()
	fileDialog.setNameFilter("GOM Element files (*.gxml);;All files (*.*)")
	if fileDialog.exec() == QFileDialog.Accepted:
		selectedFile = fileDialog.selectedFiles()[0]
		elementsFilePathEdit.setText(selectedFile)
	checkElementsFilePath()

def checkElementsFilePath():
	"""Check if elements file path is empty and enable/disable transmit button accordingly"""
	if elementsFilePathEdit.text() == "":
		elementsRequestButton.setEnabled(False)
	else:
		elementsRequestButton.setEnabled(True)

async def transmitReceive(payload):
	try:
		async with connect(URI) as websocket:
			try:
				await websocket.send(payload + '\n')
	
				response = await websocket.recv()
				outputWidget.setText(response)
			except websockets.exceptions.ConnectionClosed as e:
				outputWidget.setText(f"Connection closed: {e.code}, reason: {e.reason}")
			except Exception as e:
				outputWidget.setText(f"An error occurred: {e}")
			else:
				outputWidget.setText(response)
	except Exception as e:
		outputWidget.setText(f"An error occurred: {e}")
			
def transmitImageRequest():
	"""Create image request from user input
	"""
	request = '{"image": {'
	request += f'"file": "{imageFilePathEdit.text()}", '
	request += f'"name": "{measSeriesInput.text()}", '
	request += f'"focal_length": "{focalLengthSpinBox.value()}"'
	request += '}}'
	print(f'{request=}')
	asyncio.run(transmitReceive(request))

def transmitElementsRequest():
	"""Create elements request from user input
	"""
	request = '{"elements": {'
	request += f'"file": "{elementsFilePathEdit.text()}", '
	request += f'"import_mode": "{importModeComboBox.currentData()}"'
	request += '}}'
	print(f'{request=}')
	asyncio.run(transmitReceive(request))

#
# PySide6 GUI
#

# Create the application
app = QApplication([], windowTitle="Test Client")


# Create a layout and add the tree widget to it
layout = QVBoxLayout()

#
# Image section
#

# Header
imageLabel = QLabel("Image")
layout.addWidget(imageLabel)
line = QFrame()
line.setFrameShape(QFrame.HLine)
layout.addWidget(line)

# Image file
imageFileLabel = QLabel("File path:")
imageFilePathEdit = QLineEdit()
imageFileDialogButton = QPushButton("...")
imageFileDialogButton.setFixedWidth(25)
layout.addWidget(imageFileLabel)
hBoxLayout = QHBoxLayout()
layout.addLayout(hBoxLayout)
hBoxLayout.addWidget(imageFileDialogButton)
hBoxLayout.addWidget(imageFilePathEdit)
imageFileDialogButton.clicked.connect(openImageFileDialog)
imageFilePathEdit.editingFinished.connect(lambda: checkImageFilePath())

# Measurement Series
measSeriesLabel = QLabel("Measurement Series")
measSeriesInput = QLineEdit()
measSeriesInput.setText("Default")
hBoxLayout = QHBoxLayout()
layout.addLayout(hBoxLayout)
hBoxLayout.addWidget(measSeriesLabel)
hBoxLayout.addWidget(measSeriesInput)

# Focal Length
focalLengthLabel = QLabel("Focal Length")
focalLengthSpinBox = QDoubleSpinBox()
focalLengthSpinBox.setValue(50)
focalLengthSpinBox.setSuffix(" mm")
hBoxLayout = QHBoxLayout()
layout.addLayout(hBoxLayout)
hBoxLayout.addWidget(focalLengthLabel)
hBoxLayout.addWidget(focalLengthSpinBox)

# Transmit image request
imageRequestButton = QPushButton("Transmit image request")
imageRequestButton.clicked.connect(lambda: transmitImageRequest())
layout.addWidget(imageRequestButton)

# Spacer
spacer = QSpacerItem(20, 20)
layout.addItem(spacer)

#
# Elements section
#

# Header
elementsLabel = QLabel("Elements")
line = QFrame()
line.setFrameShape(QFrame.HLine)
layout.addWidget(elementsLabel)
layout.addWidget(line)

# Elements file
elementsFileLabel = QLabel("File path:")
elementsFilePathEdit = QLineEdit()
elementsFileDialogButton = QPushButton("...")
elementsFileDialogButton.setFixedWidth(25)
layout.addWidget(elementsFileLabel)
hBoxLayout = QHBoxLayout()
layout.addLayout(hBoxLayout)
hBoxLayout.addWidget(elementsFileDialogButton)
hBoxLayout.addWidget(elementsFilePathEdit)
elementsFileDialogButton.clicked.connect(openElementsFileDialog)
elementsFilePathEdit.editingFinished.connect(lambda: checkElementsFilePath())

# Import Mode
importModeLabel = QLabel("Import Mode")
importModeComboBox = QComboBox()
importModeComboBox.addItem("Clipboard", "clipboard")
importModeComboBox.addItem("New stage", "new_stage")
hBoxLayout = QHBoxLayout()
layout.addLayout(hBoxLayout)
hBoxLayout.addWidget(importModeLabel)
hBoxLayout.addWidget(importModeComboBox)

# Transmit elements request
elementsRequestButton = QPushButton("Transmit elements request")
elementsRequestButton.clicked.connect(lambda: transmitElementsRequest())
layout.addWidget(elementsRequestButton)

# Separator
spacer = QSpacerItem(20, 20)
layout.addItem(spacer)

#
# Status section
#

# Header
statusLabel = QLabel("Status")
line = QFrame()
line.setFrameShape(QFrame.HLine)
layout.addWidget(statusLabel)
layout.addWidget(line)

# Status output
outputWidget = QTextEdit()
outputWidget.setReadOnly(True)
outputWidget.setFixedHeight(4 * outputWidget.fontMetrics().lineSpacing())
outputWidget.setText("Ready.")
layout.addWidget(outputWidget)


#
# Window widget
#
#widget = QWidget()
widget = MyWindow()
widget.setLayout(layout)
widget.setWindowTitle("Test Client")

if elementsFilePathEdit.text() == "":
	elementsRequestButton.setEnabled(False)

if imageFilePathEdit.text() == "":
	imageRequestButton.setEnabled(False)

# Show the widget
widget.show()

# Run the event loop
app.exec()

