# WorkflowAssistants

Contains several examples for Workflow Assistants. See  [Workflow assistant](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/workflow_assistant/workflow_assistant.html)
for details. 

## List of examples

### Minimal example

The minimal example demonstrates the basic structure to create a Workflow Assistant menu structure referencing built-in commands.

The basic building blocks for the menu structure are:

1. MenuPage
    - A menu page with multiple entries that can be shown in the Workflow Assistant view.

2. NextPageEntry
    - A menu entry that allows the user to navigate to another menu or wizard page
    - Uses 'name', 'icon' and 'description' of referenced page if not given explicitly.

3. EmbeddedCommandPage
    - This is used to display a single command in the Workflow Assistant.

4. WizardPage
    - A page to show multiple commands as a sequence in a wizard layout.
    - EmbeddedCommandStep is used to represent each step
    
    
### Translation example

The translation example demonstrates the format of translatable texts in the Workflow Assistant. 
All text entries that are directly visible to the user can be given as 'TranslatableText' entry, containing the base text and a translation id.
The translation ids are resolved using the resources in the '/languages' directory.


### Custom wizard example

The 'custom_wizard' example demonstrates the creation of a script-based wizard that can be displayed in the Workflow Assistant.
These can be used to implement custom behavior for workflows.

Please see the implementation details and additional comments in the script file '/scripts/wizard_workflow.py'.


### Custom workspace with custom Workflow Assistant

The 'workspace_homepage' example demonstrates the definition of a custom workspace that references a (custom) Workflow Assistant page as its homepage.
Additional this example showcases how to reference other Workflow Assistant components in your own definitions.

## See also

* [Workflow assistant](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/workflow_assistant/workflow_assistant.html)
* [Adding workspaces to Apps](https://zeiss.github.io/zeiss-inspect-app-api/2025/howtos/adding_workspaces_to_apps/adding_workspaces_to_apps.html)