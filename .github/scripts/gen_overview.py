import os
import json


BASEDIR = 'AppExamples'

EXAMPLE_PROJECTS = {
    'zeiss_part_test_project': {'index': 1},
    'zeiss_part_test_measurement': {'index': 2},
    'volume_test_project': {'index': 3}
}

APP_OVERVIEW  = "| Category | App | Description | Example Projects | References |\n"
APP_OVERVIEW += "| -------- | --- | ----------- | ---------------- | ---------- |\n"

categories = os.listdir(BASEDIR)
for category in categories:
    #print(' Category:', category)
    #print(os.path.abspath(category))
    if os.path.isdir(os.path.abspath(os.path.join(BASEDIR, category))):
        apps = os.path.join(BASEDIR, category)
        #print(apps)
        for app in os.listdir(apps):
            #print("  App:", app)
            metainfoPath = os.path.abspath(os.path.join(BASEDIR, category, app, 'metainfo.json'))
            with open(metainfoPath, 'r', encoding="utf-8") as f:
                metainfo = json.load(f)
                #print(metainfo)
                #print(metainfo['description'])
                view = f"{category}/{app}/doc"
                download = f"https://software-store.zeiss.com/products/apps/{metainfo['title']}"

                # Category & Title, links to source code and App download 
                APP_OVERVIEW += f"| {category} | {metainfo['title']}<br>[view]({view}) / [download]({download}) | "

                # Description
                APP_OVERVIEW += f"{metainfo['description'].encode('windows-1252').decode('utf-8')} |"

                # Example projects
                if 'example-projects' in metainfo:
                    for example in metainfo['example-projects']:
                        if example in EXAMPLE_PROJECTS:
                            APP_OVERVIEW += f" {EXAMPLE_PROJECTS[example]['index']}) "
                APP_OVERVIEW += " | "
                
                # References
                if 'references' in metainfo:
                    for reference in metainfo['references']:
                        APP_OVERVIEW += f"[{reference[0]}]({reference[1]})<br>"

                APP_OVERVIEW += " |"

                APP_OVERVIEW += "\n"

# Table legend
APP_OVERVIEW += "\nExample projects\n\n"

for example in EXAMPLE_PROJECTS:
    APP_OVERVIEW += f"{EXAMPLE_PROJECTS[example]['index']}) {example}\n"

print(APP_OVERVIEW)
