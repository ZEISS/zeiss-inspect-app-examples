# -*- coding: utf-8 -*-
#
# dropdown_widget.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom


# Setup dialog from file set list of items by script
def setup_dialog():
	DIALOG = gom.script.sys.create_user_defined_dialog(file='dropdown_widget.gdlg')
	# -------------------------------------------------------------------------
	DIALOG.list.items = ['yes', 'we', 'can']
	# -------------------------------------------------------------------------
	return DIALOG


#
# Example execution
#
if __name__ == '__main__':
	DIALOG = setup_dialog()
	gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
