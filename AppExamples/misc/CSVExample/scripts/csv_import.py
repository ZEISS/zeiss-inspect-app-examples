# csv_import.py
#
# Example for importing data (in this case project keywords) from CSV file
#
# See https://docs.python.org/3/library/csv.html for details.
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_examples/
# ---

import gom
import csv

if not hasattr(gom.app, 'project'):
    gom.script.sys.execute_user_defined_dialog(file='no_project.gdlg')
    quit(0)

print("-- Current keywords --")
for k in gom.app.project.project_keywords:
    print(f"{k}='{gom.app.project.get(k)}'")


RESULT = gom.script.sys.execute_user_defined_dialog(file='import_file.gdlg')
print("\nOpening", RESULT.file)

with open(RESULT.file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if len(row) == 0:
            continue
        if len(row) != 3:
            gom.script.sys.execute_user_defined_dialog(file='wrong_format.gdlg')
            quit(0)
        key = row[0]
        desc = row[1]
        val = row[2]
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            if key != "Project Keyword" or desc != "Description" or val != "Value":
                gom.script.sys.execute_user_defined_dialog(file='wrong_format.gdlg')
                quit(0)

        else:
            # print(f'{key};{desc};{val}')
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
        line_count += 1

print("\n-- Updated keywords --")
for k in gom.app.project.project_keywords:
    print(f"{k}='{gom.app.project.get(k)}'")
