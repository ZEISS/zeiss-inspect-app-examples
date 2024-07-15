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

def gen_table(_category, _tag_index):
    """
    Generate App overview as table

    | App | Description | Example Projects | References | Tags |
    | --- | ----------- | ---------------- | ---------- | ---- |
    """
    
    # App table header
    # Using non-breaking spaces (&nbsp;) to enforce a common/minimum column width
    md  = f"| {24*'&nbsp;'}App{24*'&nbsp;'} | {36*'&nbsp;'}Description{36*'&nbsp;'} | Example Projects | References | {7*'&nbsp;'}Tags{7*'&nbsp;'} |\n"
    md +=  "| --- | ----------- | ---------------- | ---------- | ---- |\n"

    apps = os.path.join(BASEDIR, _category)
    for _app in os.listdir(apps):
        metainfo_path = os.path.abspath(os.path.join(BASEDIR, _category, _app, 'metainfo.json'))
        with open(metainfo_path, 'r', encoding="utf-8") as f:
            metainfo = json.load(f)
            if sphinx_doc:
                view = f"https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/{_category}/{_app}/doc/Documentation.md"
            else:
                view = f"{_category}/{_app}/doc/Documentation.md"
            download = f"https://software-store.zeiss.com/products/apps/{metainfo['title']}"

            # Title, links to source code and App download
            title = metainfo['title']
            md += f"| <a id=\"{title}\">{title}</a><br>[view]({view}) / [download]({download}) | "

            # Description
            md += f"{metainfo['description'].encode('windows-1252').decode('utf-8')} |"

            # Example projects
            if 'example-projects' in metainfo:
                for _example in metainfo['example-projects']:
                    if _example in EXAMPLE_PROJECTS:
                        md += f" [{EXAMPLE_PROJECTS[_example]['index']})](#example-projects) "
            md += " | "

            # References
            if 'references' in metainfo:
                for reference in metainfo['references']:
                    md += f"[{reference[0]}]({reference[1]})<br>"

            md += " | "

            # Tags
            for _tag in metainfo['tags']:
                if not _tag in _tag_index:
                    _tag_index[_tag] = []
                _tag_index[_tag].append(title)
                _badge = _tag.replace('-', '--')
                if sphinx_doc:
                    md += f"<a href=\"#{_tag}\">![Static Badge](https://img.shields.io/badge/{_badge}-blue)</a><br>"
                else:
                    md += f"[![Static Badge](https://img.shields.io/badge/{_badge}-blue)](#{_tag})<br>"
            md += " |"

            md += "\n"
    return md, _tag_index

def gen_boilerplate(_category, _tag_index):
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
    block_odd = True
    
    apps = os.path.join(BASEDIR, _category)
    for _app in os.listdir(apps):
        metainfo_path = os.path.abspath(os.path.join(BASEDIR, _category, _app, 'metainfo.json'))
        with open(metainfo_path, 'r', encoding="utf-8") as f:
            metainfo = json.load(f)
            if sphinx_doc:
                view = f"https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/{_category}/{_app}/doc/Documentation.md"
            else:
                view = f"{_category}/{_app}/doc/Documentation.md"
            download = f"https://software-store.zeiss.com/products/apps/{metainfo['title']}"

            if block_odd:
                next_class = "example-block-odd"
            else:
                next_class = "example-block-even"
            block_odd = not block_odd
            
            # Title, links to source code and App download
            title = metainfo['title']
            #md += f"### <a id=\"{title}\" class=\"link-target\">{title}</a> &mdash; [view]({view}) / [download]({download})\n\n"
            #md += f"### {title} &mdash; [view]({view}) / [download]({download})\n\n"
            md += f'<section id="{title.lower()}">\n'
            md += f'<div id="{title.lower()}" class="{next_class}">\n'
            md += \
f'''<h3>{title} — <a class="reference external" href="{view}">view</a> / 
<a class="reference external" href="{download}">download</a>
<a class="headerlink" href="#{title.lower()}" title="Link to this heading"></a></h3>
\n\n'''
            
            #md += f"![Icon](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/{category}/{app}/icon.png)\n"
            
            # Description
            md += ":Description:\n"
            md += f"    {metainfo['description'].encode('windows-1252').decode('utf-8')}\n\n"

            # Example projects
            if 'example-projects' in metainfo:
                md += ":Example Projects:\n"
                for _example in metainfo['example-projects']:
                    if _example in EXAMPLE_PROJECTS:
                        md += f"    [{_example}](#example-projects)\n"
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
                for _tag in metainfo['tags']:
                    if not _tag in _tag_index:
                        _tag_index[_tag] = []
                    _tag_index[_tag].append(title)
                    _badge = _tag.replace('-', '--')
                    if sphinx_doc:
                        md += f"<a href=\"#{_tag.lower()}\">![Static Badge](https://img.shields.io/badge/{_badge}-blue)</a> "
                    else:
                        md += f"[![Static Badge](https://img.shields.io/badge/{_badge}-blue)](#{_tag})<br> "

                md += "\n"
            md += '\n</div>\n'
            md += '\n</section>\n\n'
    
    return md, _tag_index

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
                        help='Page title')
    parser.add_argument('--meta-description', type=str,
                        default='Examples for using the ZEISS INSPECT 2025 App Python API',
                        help='Description in HTML metadata')
    # autopep8: on

    args = parser.parse_args()
    sphinx_doc = args.sphinx_doc

    app_overview = ""
    tagIndex = {}

    if sphinx_doc:
        app_overview += \
f"""---
myst:
    html_meta:
        "description": "{args.meta_description}"
        "keywords": "Metrology, ZEISS INSPECT, Python API, GOM API, Scripting, Add-ons, Apps, Examples"
---
"""

    if sphinx_doc:
        app_overview += \
"""
<style>
    .link-target {
        color: #000000;
    }
    .example-block-odd {
        background-color: #f3f6f6;
    }
    .example-block-even {
        background-color: #ffffff;
    }
</style>
"""

    app_overview += f"# {args.title}\n"

    categories = os.listdir(BASEDIR)
    for category in sorted(categories):
        if category == '.gitignore':
            continue

        if os.path.isdir(os.path.abspath(os.path.join(BASEDIR, category))):

            # Category heading
            app_overview += f"\n## {category} &mdash; {CATEGORY_DESCRIPTIONS[category]}\n\n"

            if sphinx_doc:
                tmp, tagIndex = gen_boilerplate(category, tagIndex)
            else:
                tmp, tagIndex = gen_table(category, tagIndex)
            
            app_overview += tmp

    # Example projects
    app_overview += "\n## Example projects\n\n"

    for example, infos in EXAMPLE_PROJECTS.items():
        if sphinx_doc:
            app_overview += f"* {example}\n"
        else:
            app_overview += f"{infos['index']}) {example}\n"

    app_overview += "\n[Download Example Projects App](https://software-store.zeiss.com/products/apps/ExampleProjects)"


    # Tag index
    app_overview += "\n\n## Tag Index\n"

    for tag in sorted(tagIndex):
        #app_overview += f"\n### {tag}:\n"
        badge = tag.replace('-', '--')
        if sphinx_doc:
            app_overview += f"\n### <a id=\"{tag}\">![Static Badge](https://img.shields.io/badge/{badge}-blue)<a>\n\n"
        else:
            app_overview += f"\n### ![Static Badge](https://img.shields.io/badge/{badge}-blue)\n\n"

        for app in sorted(tagIndex[tag]):
            if sphinx_doc:
                app_overview += f"* <a href=\"#{app}\">{app}</a>\n"
            else:
                app_overview += f"* [{app}](#{app})\n"
        app_overview += "\n"


    # Related links 
    app_overview += "\n## Related\n\n"
    app_overview += "* [ZEISS IQS GitHub &mdash; App Development Documentation](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/index.html)\n"
    app_overview += "* [ZEISS Quality Software Store](https://software-store.zeiss.com)\n"


    print(app_overview)
