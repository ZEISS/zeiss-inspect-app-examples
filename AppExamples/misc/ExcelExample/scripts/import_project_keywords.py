# -*- coding: utf-8 -*-
#
# import_project_keywords.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import datetime
import re

from openpyxl import load_workbook

if not hasattr(gom.app, 'project'):
    gom.script.sys.execute_user_defined_dialog(file='no_project.gdlg')
    quit(0)

print("-- Current keywords --")
for k in gom.app.project.project_keywords:
    print(f"{k}='{gom.app.project.get(k)}'")

# Cells containing the keywords - columns are currently restricted to 'A'-'Z'!
# - descriptions are expected in column+1
# - values are expected in column+2
layout = [
    "A2",
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    "A9",
    "A10",
    "A11",
    "A12"
]


def add_column(cell, offs):
    '''Adds an offset to the column of a cell designator, currently only A-Z supported'''
    p = re.compile('(\D+)(\d+)')
    m = p.match(cell)
    col = m.group(1)
    col = chr(ord(col) + offs)
    row = m.group(2)
    return f'{col}{row}'


RESULT = gom.script.sys.execute_user_defined_dialog(file='import_file.gdlg')
print("\nOpening", RESULT.file)

wb = load_workbook(filename=RESULT.file)
sheet = wb['Sheet']

print("\n-- Importing keywords --")
for cell in layout:
    key = sheet[cell].value
    desc = sheet[add_column(cell, 1)].value
    val = sheet[add_column(cell, 2)].value
    # print(f"{key} - {desc}: {val}")
    if type(val) is datetime.datetime:
        val = val.strftime("%Y-%m-%d")
    elif val is None or val == 'None':
        val = ""
    else:
        val = str(val)

    ukw = "user_" + key
    if not ukw in gom.app.project.project_keywords:
        print(f"New keyword {key}='{val}' added")
        gom.script.sys.set_project_keywords(keywords={key: val}, keywords_description={key: desc})
    else:
        ex_val = gom.app.project.get(ukw)
        if val != ex_val:
            print(f"Existing keyword {key}='{ex_val}' changed to '{val}'")
            gom.script.sys.set_project_keywords(keywords={key: val})
        else:
            print(f"Existing keyword {key}='{val}' - not changed")

print("\n-- Updated keywords --")
for k in gom.app.project.project_keywords:
    print(f"{k}='{gom.app.project.get(k)}'")
