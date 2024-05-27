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
print('Files in directory tree below', dir + ':')
for (basepath, subfolders, filenames) in os.walk(dir):
	print('  Files in directory', basepath + ':')
	for filename in filenames:
		base, ext = os.path.splitext(filename)
		print('    File:', filename, '  Base:', base, '  Extension:', ext)
		print('      -> Full path:', os.path.join(basepath, filename))
