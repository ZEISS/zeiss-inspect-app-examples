# -*- coding: utf-8 -*-
#
# test_data_interfaces_volume_section.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import numpy as np

from addon import ArrayDataTest, ElementTest
from ExampleProjects.setup_project import open_project

# Importing the example we want to test
import volume_section_image_data as example


def test_volume_section():
    # Setup test project
    open_project('volume_test_project')
    test_element = gom.app.project.actual_elements['Plane X +40.00 mm']
    #
    # TEST
    #
    element_test = ElementTest('test_data/data_interfaces_volume_section_tokens.dat')
    element_test.testElementValues(test_element, ['image_width', 'image_height', 'image_type'])
    element_test.callTest()

    raw_array = example.get_image_data_raw(test_element)
    raw_array_test = ArrayDataTest('test_data/data_interfaces_volume_section_raw.dat')
    raw_array_test.testArrayValues(raw_array)

    rgb_array = example.get_image_data_rgb(test_element)
    rgb_array_test = ArrayDataTest('test_data/data_interfaces_volume_section_rgb.dat')
    rgb_array_test.testArrayValues(rgb_array)
