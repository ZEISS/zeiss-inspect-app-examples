# -*- coding: utf-8 -*-
#
# service.py
#
# OSM Map Diagram Service (Scripted Diagram)
# Uses Cartopy https://scitools.org.uk/cartopy/docs/latest/index.html
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import io
import gom
from gom import apifunction
import gom.api.settings
    
import matplotlib.pyplot as plt
import numpy as np

import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt


# Set path for debugging
SVG_PATH = None
#SVG_PATH = 'C:/temp/OSMMapDiagram.svg'

# Set SVG resolution in dpi
SVG_DPI = 'figure'

ALTITUDE = gom.tr("Alt.")

# helper function
def zoomlevel_from_deg(delta):
    """Calculate OSM zoom level from a span in degrees.  Adjust +/-1 as desired"""
    from numpy import log2, clip, floor
    zoomlevel = int(clip(floor(log2(360) - log2(delta)),0,20 ))
    return zoomlevel 

def meters_to_deg(dist):
    """Degrees (latitude) assuming spherical earth model"""
    return dist * 360 / (2 * np.pi * 6400000)
    
@apifunction
def geolocation(*args, **kwargs)->str:
    """Create OSM map diagram with location markers and (optional) labels
    
    Args:
        *args (any): (unused)
        **kwargs (dict): 
          {
            '<uuid>': {
              'ude_diagram_alt': 0.0,
              'ude_diagram_alt_en': False, 
              'ude_diagram_custom': 1,
              'ude_diagram_label': '<label>',
              'ude_diagram_lat': <latitude>,
              'ude_diagram_lon': <longitude>,
              ...
            },
            ..
          }

    Returns:
        string: SVG image
    """
    gom.log.info('Geolocation Service')
    gom.log.info(f'{kwargs=}')
    request = cimgt.OSM()
    
    # Find bounding box
    lat_min = 90
    lat_max = -90
    lon_min = 180
    lon_max = -180
    for element in kwargs.keys():
        gom.log.info(f'{kwargs[element]=}')
        lat = kwargs[element]['ude_diagram_lat']
        lat_min = min(lat_min, lat)
        lat_max = max(lat_max, lat)
        gom.log.debug(f'{lat=}')
        lon = kwargs[element]['ude_diagram_lon']
        gom.log.debug(f'{lon=}')
        lon_min = min(lon_min, lon)
        lon_max = max(lon_max, lon)
    
    gom.log.debug(f'{lat=}, {lon=}')
    gom.log.debug(f'lat: {lat_min}..{lat_max} lon: {lon_min}..{lon_max}')
    lat_center = (lat_min + lat_max) / 2
    lon_center = (lon_min + lon_max) / 2
    
    # Set map range and aspect ratio
    range = gom.api.settings.get('range')
    aspect = gom.api.settings.get('aspect')
    
    delta = meters_to_deg(range)
    zoom = zoomlevel_from_deg(delta)-1 #  0-19 
    gom.log.debug(f'Zoom Level: {zoom}')

    # Bounds: (lon_min, lon_max, lat_min, lat_max):
    delta_lat = delta / aspect
    extent = [lon_center-delta/np.cos(lat_center*np.pi/180), lon_center+delta/np.cos(lat_center*np.pi/180), lat_center-delta_lat, lat_center+delta_lat]

    # See https://scitools.org.uk/cartopy/docs/latest/reference/generated/cartopy.mpl.geoaxes.GeoAxes.html#cartopy-mpl-geoaxes-geoaxes
    ax = plt.axes(projection=request.crs)
    ax.set_extent(extent)
    
    # Add map tiles
    # See https://scitools.org.uk/cartopy/docs/latest/reference/generated/cartopy.mpl.geoaxes.GeoAxes.html#cartopy.mpl.geoaxes.GeoAxes.add_image
    ax.add_image(request, zoom)

    # Location marker (see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
    marker_style = gom.api.settings.get('marker_style')
    marker_color = gom.api.settings.get('marker_color')
    marker_size = gom.api.settings.get('marker_size')

    # Add location markers and (optional) labels
    for element in kwargs.keys():
        gom.log.debug(f'{kwargs[element]=}')
        lat = kwargs[element]['ude_diagram_lat']
        lon = kwargs[element]['ude_diagram_lon']
        alt_en = kwargs[element]['ude_diagram_alt_en']
        alt = kwargs[element]['ude_diagram_alt']
        if alt_en:
            alt = alt
        else:
            alt = None 
        gom.log.debug(f'{alt=}')
        label = kwargs[element]['ude_diagram_label']
        
        # Add label and/or altitude as annotation
        annotation = ""
        if label and alt:
            annotation = f'{label}\n{ALTITUDE}: {alt}'
        elif label:
            annotation = label
        elif alt:
            annotation = f'{ALTITUDE}: {alt}'
        
        # Location label offset
        label_xoffset = gom.api.settings.get('label_xoffset')
        label_yoffset = gom.api.settings.get('label_yoffset')
    
        if annotation != "":
            # see https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html
            ax.annotate(
                annotation,
                xy=(lon, lat), transform=ccrs.PlateCarree(),
                xytext=(label_xoffset, label_yoffset),
                textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle="->", shrinkA=5, shrinkB=5)
    
        # Add a marker at the current geolocation
        plt.scatter(lon, lat, transform=ccrs.PlateCarree(), marker=marker_style, s=marker_size, c=marker_color)
    
    title = gom.api.settings.get('title')
    plt.title(title)
    copyright_text = "Map data © OpenStreetMap contributors"
    ax.text(0, -0.03, copyright_text, transform=ax.transAxes, ha='left', fontsize=8)

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

