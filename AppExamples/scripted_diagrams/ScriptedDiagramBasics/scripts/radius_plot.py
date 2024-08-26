# -*- coding: utf-8 -*-
#
# radius_histogram.py
#
# Service function which receives the radii of all elements plots
# radius and element name.
# See https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---
"""Scripted diagram service plotting radius / element name"""

import io
import gom
from gom import apifunction
import matplotlib.pyplot as plt


# Set path for debugging
SVG_PATH = None
#SVG_PATH = 'C:/temp/ScriptedDiagram.svg'

# Set SVG resolution in dpi
SVG_DPI = 'figure'

def filter_all(k, v):
    """Filter all elements by key, value
    
     Args:
        k (string): key
        v (any): value

    Returns:
        list: element references
    """
    r = []
    for g in [gom.app.project.nominal_elements, gom.app.project.inspection, gom.app.project.actual_elements]:
        r += g.filter(k, v)
    return r

@apifunction
def radius_plot(*args, **kwargs)->str:
    """Plot a radius histogram
    
    Args:
        args (any): (unused)
        kwargs (dict): {'<uuid>': {'ude_diagram_custom': 1, 'ude_diagram_radius': <radius>, ...}, ...}

    Returns:
        string: SVG image
    """
    gom.log.info('Radius Plot Service')
    gom.log.info(f'{kwargs=}')

    radius = []
    elementnames = []    
    for uuid, params in kwargs.items():
        element = filter_all('uuid_draft', uuid)[0]
        elementnames.append(element.name)
        radius.append(params['ude_diagram_radius'])

    # create x/y plot
    plt.figure(figsize = (10, 5))
    plt.plot(elementnames, radius, 'bx')
    plt.xticks(rotation = 90)
    plt.subplots_adjust(bottom=0.2)

    if SVG_PATH:
        plt.savefig(SVG_PATH, format='svg', dpi=SVG_DPI)

    # Create an empty file-like object
    svg_output = io.StringIO()

    # Save the plot to the file-like object
    plt.savefig(svg_output, format='svg', dpi=SVG_DPI)

    # Get the SVG string from the file-like object
    svg_string = svg_output.getvalue()

    # Close the file-like object
    svg_output.close()

    return svg_string

gom.run_api()
