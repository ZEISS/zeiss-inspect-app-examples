# -*- coding: utf-8 -*-
#
# volume_section_image_data.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import numpy as np
from ExampleProjects.setup_project import open_project
from PIL import Image # Package: pillow


def get_image_data_rgb(el):
    """Get the image in RGB(A) format (rendered image as displayed)
    """
    # -------------------------------------------------------------------------
    img = np.array(el.data.rgb)
    # -------------------------------------------------------------------------
    return img

def get_image_data_raw(el):
    """Get the image in raw format (values as in the corresponding volume)
    """
    # -------------------------------------------------------------------------
    img = np.array(el.data.raw)
    # -------------------------------------------------------------------------
    return img


#
# Example execution
#
if __name__ == '__main__':
    open_project('volume_test_project')

    # Generating a dialog for user selection of a volume section
    DIALOG = gom.script.sys.create_user_defined_dialog(file='volume_section_image_data.gdlg')

    def volume_section_filter(element):
        try:
            return element.type == "volume_section"
        except:
            pass
        return False

    DIALOG.section.filter = volume_section_filter
    RESULT = gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    element = RESULT.section

    if element is not None:
        # Getting some image properties
        # -------------------------------------------------------------------------
        print('Height: ', element.image_height)
        print('Width: ', element.image_width)
        print('Type: ', element.image_type)
        # -------------------------------------------------------------------------

        rgb_image = get_image_data_rgb(element)
        raw_image = get_image_data_raw(element)

        # The RGBA image can also be used with other libraries,
        # e.g. Pillow
        Image.fromarray(rgb_image[0]).show()

        print("Raw image (Token: rgb), dtype=", rgb_image.dtype, ", shape=", rgb_image.shape)
        print("Rendered image (Token: render), dtype=", raw_image.dtype, ", shape=", raw_image.shape)
    else:
        print("No volume section selected")
