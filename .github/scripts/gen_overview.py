#
# gen_overview.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# ---
'''Generate ZEISS INSPECT App Examples Overview markdown file'''

import os
import json
import argparse


BASEDIR = 'AppExamples'

CATEGORY_DESCRIPTIONS = {
    'data_interfaces': 'How to access data of ZEISS INSPECT elements',
    'dialog_widgets': 'How to use custom dialogs and handle user input events',
    'misc': 'Miscellaneous',
    'script_icons': 'How to set icons for scripts or buttons',
    'script_resources': 'How to access binary data of your App (resources)',
    'scripted_actuals': 'Building custom actual elements with Python code',
    'scripted_checks': 'Building custom checks with Python code',
    'projects': 'ZEISS INSPECT projects'
}

EXAMPLE_PROJECTS = {
    'zeiss_part_test_project': {'index': 1},
    'zeiss_part_test_measurement': {'index': 2},
    'volume_test_project': {'index': 3}
}

def gen_table(category):
    """
    Generate App overview as table

    | App | Description | Example Projects | References | Tags |
    | --- | ----------- | ---------------- | ---------- | ---- |
    """

    # App table header
    # Using non-breaking spaces (&nbsp;) to enforce a common/minimum column width
    md  = f"| {24*'&nbsp;'}App{24*'&nbsp;'} | {36*'&nbsp;'}Description{36*'&nbsp;'} | Example Projects | References | {7*'&nbsp;'}Tags{7*'&nbsp;'} |\n"
    md +=  "| --- | ----------- | ---------------- | ---------- | ---- |\n"

    apps = os.path.join(BASEDIR, category)
    for app in os.listdir(apps):
        metainfo_path = os.path.abspath(os.path.join(BASEDIR, category, app, 'metainfo.json'))
        with open(metainfo_path, 'r', encoding="utf-8") as f:
            metainfo = json.load(f)
            if sphinx_doc:
                view = f"https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/{category}/{app}/doc/Documentation.md"
            else:
                view = f"{category}/{app}/doc/Documentation.md"
            download = f"https://software-store.zeiss.com/products/apps/{metainfo['title']}"

            # Title, links to source code and App download
            title = metainfo['title']
            md += f"| <a id=\"{title}\">{title}</a><br>[view]({view}) / [download]({download}) | "

            # Description
            md += f"{metainfo['description'].encode('windows-1252').decode('utf-8')} |"

            # Example projects
            if 'example-projects' in metainfo:
                for example in metainfo['example-projects']:
                    if example in EXAMPLE_PROJECTS:
                        md += f" [{EXAMPLE_PROJECTS[example]['index']})](#example-projects) "
            md += " | "

            # References
            if 'references' in metainfo:
                for reference in metainfo['references']:
                    md += f"[{reference[0]}]({reference[1]})<br>"

            md += " | "

            # Tags
            for tag in metainfo['tags']:
                if not tag in tagIndex:
                    tagIndex[tag] = []
                tagIndex[tag].append(title)
                badge = tag.replace('-', '--')
                if sphinx_doc:
                    md += f"<a href=\"#{tag}\">![Static Badge](https://img.shields.io/badge/{badge}-blue)</a><br>"
                else:
                    md += f"[![Static Badge](https://img.shields.io/badge/{badge}-blue)](#{tag})<br>"
            md += " |"

            md += "\n"
            return md

def gen_boilerplate(category):
    """
        Generate App overview as table

        ### App 
        
        Description
            ...

        Example Projects
            ...
        
        References
            ...
        
        Tags
            ...
    """

    md = ""

    apps = os.path.join(BASEDIR, category)
    for app in os.listdir(apps):
        metainfo_path = os.path.abspath(os.path.join(BASEDIR, category, app, 'metainfo.json'))
        with open(metainfo_path, 'r', encoding="utf-8") as f:
            metainfo = json.load(f)
            if sphinx_doc:
                view = f"https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/{category}/{app}/doc/Documentation.md"
            else:
                view = f"{category}/{app}/doc/Documentation.md"
            download = f"https://software-store.zeiss.com/products/apps/{metainfo['title']}"

            # Title, links to source code and App download
            title = metainfo['title']
            md += f"### <a id=\"{title}\">{title}</a> &mdash; [view]({view}) / [download]({download})\n\n"

            #md += f"![Icon](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/{category}/{app}/icon.png)\n"

            # Description
            md += ":Description:\n"
            md += f"    {metainfo['description'].encode('windows-1252').decode('utf-8')}\n\n"

            # Example projects
            if 'example-projects' in metainfo:
                md += ":Example Projects:\n"
                for example in metainfo['example-projects']:
                    if example in EXAMPLE_PROJECTS:
                        md += f"    [{example}](#example-projects)\n"
                md += "\n"
            
            # References
            if 'references' in metainfo:
                md += ":References:\n"
                for reference in metainfo['references']:
                    md += f"    [{reference[0]}]({reference[1]})\n"

                md += "\n"

            # Tags
            if len(metainfo['tags']):
                md += ":Tags:\n"
                md += "    "
                for tag in metainfo['tags']:
                    if not tag in tagIndex:
                        tagIndex[tag] = []
                    tagIndex[tag].append(title)
                    badge = tag.replace('-', '--')
                    if sphinx_doc:
                        md += f"<a href=\"#{tag}\">![Static Badge](https://img.shields.io/badge/{badge}-blue)</a> "
                    else:
                        md += f"[![Static Badge](https://img.shields.io/badge/{badge}-blue)](#{tag})<br> "

                md += "\n"
    return md

# ----------------------------------------------------------------------------
# MAIN
#
if __name__ == '__main__':
    #
    # Parse command line arguments
    #
    parser = argparse.ArgumentParser()

    # autopep8: off
    parser.add_argument('--sphinx-doc', action='store_true', help='Select sphinx_doc layout')
    parser.add_argument('--title', type=str,
                        default='ZEISS INSPECT App Examples Overview',
                        help='Python wheelhouse directory')
    # autopep8: on

    args = parser.parse_args()
    sphinx_doc = args.sphinx_doc

    APP_OVERVIEW = ""

    if sphinx_doc:
        APP_OVERVIEW += \
    """---
    myst:
    html_meta:
        "description": "Examples for using the ZEISS INSPECT 2025 App Python API"
        "keywords": "Metrology, ZEISS INSPECT, Python API, GOM API, Scripting, Add-ons, Apps, Examples"
    ---
    """

    APP_OVERVIEW += f"# {args.title}\n"

    tagIndex = {}

    categories = os.listdir(BASEDIR)
    for category in categories:
        if category == '.gitignore':
            continue

        if os.path.isdir(os.path.abspath(os.path.join(BASEDIR, category))):

            # Category heading
            APP_OVERVIEW += f"\n## {category} &mdash; {CATEGORY_DESCRIPTIONS[category]}\n\n"

            if sphinx_doc:
                APP_OVERVIEW += gen_boilerplate(category)
            else:
                APP_OVERVIEW += gen_table(category)


    # Example projects
    APP_OVERVIEW += "\n## Example projects\n\n"

    for example, infos in EXAMPLE_PROJECTS.items():
        if sphinx_doc:
            APP_OVERVIEW += f"* {example}\n"
        else:
            APP_OVERVIEW += f"{infos['index']}) {example}\n"

    APP_OVERVIEW += "\n[Download Example Projects App](https://software-store.zeiss.com/products/apps/ExampleProjects)"


    # Tag index
    APP_OVERVIEW += "\n\n## Tag Index\n"

    for tag in sorted(tagIndex):
        #APP_OVERVIEW += f"\n### {tag}:\n"
        badge = tag.replace('-', '--')
        if sphinx_doc:
            APP_OVERVIEW += f"\n### <a id=\"{tag}\">![Static Badge](https://img.shields.io/badge/{badge}-blue)<a>\n\n"
        else:
            APP_OVERVIEW += f"\n### ![Static Badge](https://img.shields.io/badge/{badge}-blue)\n\n"

        for app in sorted(tagIndex[tag]):
            if sphinx_doc:
                APP_OVERVIEW += f"* <a href=\"#{app}\">{app}</a>\n"
            else:
                APP_OVERVIEW += f"* [{app}](#{app})\n"
        APP_OVERVIEW += "\n"


    # Related links 
    APP_OVERVIEW += "\n## Related\n\n"
    APP_OVERVIEW += "* [ZEISS IQS GitHub &mdash; App Development Documentation](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/index.html)\n"
    APP_OVERVIEW += "* [ZEISS Quality Software Store](https://software-store.zeiss.com)\n"


    print(APP_OVERVIEW)
