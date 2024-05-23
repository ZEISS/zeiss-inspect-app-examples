# -*- coding: utf-8 -*-
#
# This script demonstrates reading asset or resource data from a package
#

import gom

#
# Resources are addressed with a relative or absolute file system path
#
data = gom.app.resource["assets/zeiss_logo.png"]

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


