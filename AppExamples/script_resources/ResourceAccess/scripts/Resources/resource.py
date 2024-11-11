# -*- coding: utf-8 -*-
#
# resource.py
#
# This script demonstrates reading an asset or resource data from an App
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom

#
# Resources are addressed with a relative or absolute file system path.
#
resource = gom.Resource("assets/zeiss_logo.png")
with resource.open() as fh:
    data = fh.read()

resource.close()

print ('Type:', type (data))
print ('Size:', len (data))

#
# Use script dialog to display the resource as an image. The 'data' field of
# the image widget expects a displayable byte object and will render it.
#
DIALOG=gom.script.sys.create_user_defined_dialog (file='dialog.gdlg')

DIALOG.image.data = data

#
# After dialog setup, it can be displayed.
#
gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
