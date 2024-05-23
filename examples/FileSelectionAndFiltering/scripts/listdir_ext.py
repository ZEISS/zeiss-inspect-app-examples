# -*- coding: utf-8 -*-

import gom
import os


RESULT=gom.script.sys.execute_user_defined_dialog (dialog={
	"content": [
		[
			{
				"columns": 1,
				"default": "",
				"file_types": [
				],
				"file_types_default": "",
				"limited": False,
				"name": "directory",
				"rows": 1,
				"selection_type": "directory",
				"title": {
					"id": "",
					"text": "Choose Folder",
					"translatable": True
				},
				"tooltip": {
					"id": "",
					"text": "Click to select a folder",
					"translatable": True
				},
				"type": "input::file"
			}
		]
	],
	"control": {
		"id": "OkCancel"
	},
	"embedding": "",
	"position": "",
	"size": {
		"height": 112,
		"width": 271
	},
	"sizemode": "",
	"style": "Standard",
	"title": {
		"id": "",
		"text": "List files in a folder",
		"translatable": True
	}
})

dir = RESULT.directory
# change working directory to the selected directory
os.chdir(dir)
print('Files in directory', dir + ':')
for filename in os.listdir(dir):
	if os.path.isdir(filename):
		print('  Folder:', filename)
	elif os.path.isfile(filename):
		base, ext = os.path.splitext(filename)
		print('    File:', filename, '  Base:', base, '  Extension:', ext)
	else:
		print('   Other:', filename)
