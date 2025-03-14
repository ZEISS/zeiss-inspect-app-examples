# -*- coding: utf-8 -*-
#
# uut_project_keywords.py
#
# Unit Under Test (UUT) Example
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# ---

import gom


####################################################################################
# Note: This entire script is run by test_blackbox
####################################################################################

# Create a new project. This will rais an exception if a project is already open - which is fine.
try:
    gom.script.sys.create_project ()
except:
    pass

def not_covered_by_test():
    '''This is not covered by any test'''
    print("Hello")

def excluded_from_coverage(): # pragma: no cover
    '''This is not covered by any test either, but won't contribute to the coverage'''
    print("Nothing to say")

def get_project_keywords():
    '''This is called by test_whitebox'''
    keywords = {}
    for k in gom.app.project.project_keywords:
        keywords[k] = {
            'description': gom.app.project.get(f'description({k})'),
            'value': gom.app.project.get(k)
        }
    print(keywords)
    return keywords

PROJECT_KEYWORDS = {
    'project': {'description': 'Project Name', 'value': 'Test Project'},
    'inspector': {'description': 'Inspector', 'value': 'Clouseau'}
}

for k, v in PROJECT_KEYWORDS.items():
    gom.script.sys.set_project_keywords(
        keywords={k:v['value']},
        keywords_description={k:v['description']}
    )

print("-- Project keywords --")
for k in gom.app.project.project_keywords:
    print(f"{k}='{gom.app.project.get(k)}'")
