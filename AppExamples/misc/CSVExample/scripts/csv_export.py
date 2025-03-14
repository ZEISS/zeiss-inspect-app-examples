# csv_export.py
#
# Example for exporting data (in this case project keywords) as CSV file
#
# See https://docs.python.org/3/library/csv.html for details.
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import csv
import datetime

if not hasattr(gom.app, 'project'):
    gom.script.sys.execute_user_defined_dialog(file='no_project.gdlg')
    quit(0)

# File selection dialog
RESULT = gom.script.sys.execute_user_defined_dialog(file='export_file.gdlg')

with open(RESULT.file, mode='w', newline='') as keywords_file:
    keywords_writer = csv.writer(keywords_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Header row
    keywords_writer.writerow(['Project Keyword', 'Description', 'Value'])

    for key in gom.app.project.project_keywords:
        val = gom.app.project.get(key)
        desc = gom.app.project.get(f'description({key})')

        # Remove prefix 'user_' from key
        key = key[5:]
        print(f"{key} - {desc}: {val}")

        # Special case - convert gom.Date to datetime-object
        if type(val) is gom.Date:
            val = datetime.datetime(val.year, val.month, val.day)

        # Write next row
        keywords_writer.writerow([key, desc, val])
