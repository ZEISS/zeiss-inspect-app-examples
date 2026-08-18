# -*- coding: utf-8 -*-
#
# create_surface.py
#
# Example for creating a scripted surface element
#
# See https://zeiss.github.io/zeiss-inspect-app-api/2026/python_api/scripted_elements_api.html#surface
#
# Carl Zeiss GOM Metrology GmbH, 2026
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2026/python_examples/examples_overview.html
# ---

import gom


# -------------------------------------------------------------------------
def calculation(context, params):
    valid_results = False

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {
                'vertices': params['vertices'],
                'triangles': params['triangles']
            }
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
# -------------------------------------------------------------------------
