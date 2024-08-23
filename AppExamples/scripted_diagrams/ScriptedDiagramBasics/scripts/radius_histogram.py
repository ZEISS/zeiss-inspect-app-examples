# -*- coding: utf-8 -*-
#
# radius_histogram.py
#
# Service function which receives the radii of all elements and generates a histogram
# Diagram settings are available in Preferences->App-Settings->ScriptedDiagramBasics
# See https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---
"""Scripted diagram service creating a radius histogram"""

import io
import gom
import gom.api.settings
from gom import apifunction
import matplotlib.pyplot as plt

# Set path for debugging
SVG_PATH = None
#SVG_PATH = 'C:/temp/OSMMapDiagram.svg'

# Set SVG resolution in dpi
SVG_DPI = 'figure'

@apifunction
def radius_histogram(*args, **kwargs)->str:
    """Plot element name/radius
    
    Args:
        args (any): (unused)
        kwargs (dict): {'<uuid>': {'ude_diagram_custom': 1, 'ude_diagram_radius': <radius>, ...}, ...}

    Returns:
        string: SVG image
    """
    gom.log.info('Radius Histogram Service')
    gom.log.info(f'{kwargs=}')
    bins = gom.api.settings.get('bins')
    bins = [int(elem) for elem in bins.split(',') if elem.strip().isnumeric()]
    radius = []

    for uuid, params in kwargs.items():
        radius.append(params['ude_diagram_radius'])

    gom.log.debug(f'{bins=}')
    gom.log.debug(f'{radius=}')

    plt.figure(figsize = (10, 5))
    color =  gom.api.settings.get('barcolor')

    # Creating the histogram plot
    nbins, bins, _ = plt.hist(radius, bins=bins, color = color, rwidth=0.5)
    gom.log.debug(f'{nbins=},{bins=}')
    plt.title(gom.api.settings.get('title'))
    plt.xlabel(gom.api.settings.get('xlabel'))
    plt.ylabel(gom.api.settings.get('ylabel'))

    # Create customized x-ticks
    xticks = []
    xlabels = []
    for i in range(len(nbins)):
        xticks.append((bins[i] + bins[i+1])/2)
        if i < len(nbins)-1:
            # All but last bin:
            # Interval [n, n+1)
            xlabels.append(f'[{bins[i]},{bins[i+1]})')
        else:
            # Last bin:
            # Interval [n, n+1]
            xlabels.append(f'[{bins[i]},{bins[i+1]}]')
    plt.xticks(xticks, xlabels)

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