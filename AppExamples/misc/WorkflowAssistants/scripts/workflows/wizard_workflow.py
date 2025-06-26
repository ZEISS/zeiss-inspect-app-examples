# -*- coding: utf-8 -*-

import gom

#
# This is an example for a custom wizard-based workflow.
# It showcases the basic control flow of the wizard.
#

#
# First, create the user defined dialog to display.
# The variable 'DIALOG' is needed to have access to the various widgets inside the dialog.
#
# A few points are important here to correctly display the wizard as part of the Workflow Assistant:
#
#   1. The type should be 'Dialog without control buttons'
#
#   2. The 'embedding' mode of the dialog should be 'Embedded as widget'
#
#   3. The top-level widget of the dialog should be a single wizard layout
#
#   4. Every other widget to be displayed is part of some step of the wizard layout
#
DIALOG = gom.script.sys.create_user_defined_dialog(file="wizard_workflow.gdlg")


#
# Next, we can define aliases for the step ids to make the following easier to read.
# The steps are given integer ids in the order they are defined in the dialog editor, starting with 0.
#
INITIAL_STEP = 0
OPTIONAL_STEP = 1
DECIDER_STEP = 2
OPTION_A_STEP = 3
OPTION_B_STEP = 4
BRANCHING_STEP = 5
NEXT_STEP = 6
ALTERNATIVE_STEP = 7
FINAL_STEP = 8


#
# Now we define a few event handler functions that can react to actions by the user.
# These can be attached to (one or more) individual dialog widgets to only receive events from those specific widgets.
#
# We can also attache one handler to the dialog itself.
# In this handler the widget argument can then be checked against the widgets we want to react to.
#

#
# Before a user is allowed to proceed to the next step, they usually have to complete one ore more actions.
# Here they just have to flip a toggle button.
# The handler connected to that button then sets the complete state of the step, which enables the next button.
# We could also connect the same handler to multiple widgets in one step to check if their values are all valid.
# We would then need to access them via the dialog object instead of the widget parameter.
#
def complete_current_if_true(widget):
    '''
    Check if the value of the widget is a bool and set the current wizard step to complete if it is true
    '''
    if isinstance(widget.value, bool):
        DIALOG.wizard.step_set_complete(DIALOG.wizard.current_id, widget.value)


DIALOG.checkbox_1.handler = complete_current_if_true
DIALOG.checkbox_2.handler = complete_current_if_true


#
# In this example a text field is used, which requires a non-empty value.
#
def complete_current_if_text_set(widget):
    '''
    Check if the value of the widget is a string and set the current wizard step to complete if it is non-empty
    '''
    if isinstance(widget.value, str):
        complete = len(widget.value) > 0
        DIALOG.wizard.step_set_complete(DIALOG.wizard.current_id, complete)


DIALOG.text_1.handler = complete_current_if_text_set
DIALOG.text_2.handler = complete_current_if_text_set


#
# In another step, a button press should trigger some action in the SW. Here a small info dialog is opened.
#
def button_handler(widget):
    '''
    On a button press, trigger some action and set the current wizard step to complete
    '''
    gom.script.sys.execute_user_defined_dialog(file='info_dialog.gdlg')
    DIALOG.wizard.step_set_complete(DIALOG.wizard.current_id, True)


DIALOG.button.handler = button_handler


#
# This step is optional. It can be completed but it can also be skipped.
#
DIALOG.wizard.step_set_optional(OPTIONAL_STEP, True)


#
# If the skip button is set to be separate, the step can be skipped event if it is complete.
# This is useful if the widgets all have sensible default values and the user might still want to skip the step.
#
def separate_skip_button(widget):
    DIALOG.wizard.step_set_skip_button_separate(OPTIONAL_STEP, widget.value)


DIALOG.separate_skip_button.handler = separate_skip_button


#
# The steps are normally visited in the order of their ids, which is the order from the dialog editor.
# We can however also override that order by changing the next id of a step.
#
DIALOG.wizard.step_set_next_id(INITIAL_STEP, OPTIONAL_STEP)


#
# We can set the next step in the handler to make the step order dynamic based on user input.
# For example, here a selection list is used to define the next step of the wizard.
#
def list_1_handler(widget):
    '''
    Change the next step depending on the selected list element
    '''
    if widget.value == 'Option A':
        DIALOG.wizard.step_set_next_id(DECIDER_STEP, OPTION_A_STEP)
    elif widget.value == 'Option B':
        DIALOG.wizard.step_set_next_id(DECIDER_STEP, OPTION_B_STEP)


DIALOG.list_1.handler = list_1_handler

#
# We want both branches to lead back to the same step.
# Since OPTION_B_STEP would be the next step after OPTION_A_STEP, we need to change it to the one after that.
#
DIALOG.wizard.step_set_next_id(OPTION_A_STEP, BRANCHING_STEP)


#
# Another way to diverge the flow of the wizard is using the branch button.
# It represents an alternative path from this step or an optional action the user can take in this step.
#
DIALOG.wizard.step_set_branch_button_visible(BRANCHING_STEP, True)
DIALOG.wizard.step_set_branch_button_text(BRANCHING_STEP, 'Branch')
DIALOG.wizard.step_set_branch_id(BRANCHING_STEP, ALTERNATIVE_STEP)


#
# The paths may or may not join together after diverging.
#
DIALOG.wizard.step_set_next_id(NEXT_STEP, FINAL_STEP)


#
# The branch button may also be used to skip over the next step or insert an additional step.
#
# DIALOG.wizard.step_set_next_id(BRANCHING_STEP, FINAL_STEP)
# DIALOG.wizard.step_set_branch_id(BRANCHING_STEP, FINAL_STEP)


#
# The enabled state of the branch button can and has to be set separately from the complete state of the step.
# It is enabled by default.
#
DIALOG.wizard.step_set_branch_button_enabled(BRANCHING_STEP, False)


def complete_with_branch_button(widget):
    DIALOG.wizard.step_set_branch_button_enabled(BRANCHING_STEP, widget.value)
    DIALOG.wizard.step_set_complete(BRANCHING_STEP, widget.value)


DIALOG.checkbox_branch.handler = complete_with_branch_button


#
# The next button also does not always have to be labeled as such.
# We can then also set steps completed from the start of course.
#
DIALOG.wizard.step_set_next_button_text(NEXT_STEP, "Do the thing")
DIALOG.wizard.step_set_next_button_text(ALTERNATIVE_STEP, "Do the other thing")
DIALOG.wizard.step_set_complete(NEXT_STEP, True)
DIALOG.wizard.step_set_complete(ALTERNATIVE_STEP, True)


#
# Normally the wizard starts with step 0, but this can also be overridden.
# Although this has no effect once the wizard dialog is shown, so it can not be used in a handler.
#
DIALOG.wizard.start_id = INITIAL_STEP


#
# The last step is automatically set to final, that means that it has a finish button, which ends the wizard dialog successfully.
# We can also make any other step final by calling this method.
#
DIALOG.wizard.step_set_final(FINAL_STEP, True)

DIALOG.wizard.step_set_complete(FINAL_STEP, True)


#
# The branch button can also be used to trigger an entirely different action.
# This is usually done on a final step to let the user immediately continue to another workflow or switch to a different workspace.
# We simply have to not set the branch id and then react to the branched event in the wizard handler, as seen below.
#
DIALOG.wizard.step_set_branch_button_visible(FINAL_STEP, True)
DIALOG.wizard.step_set_branch_button_text(FINAL_STEP, "Deviation Labels")


#
# To react to events from the wizard itself, a separate event handler is used.
# In the case of the wizard the argument of this handler is a dict, which contains the following keys:
# - widget: is the wizard widget
# - step: is the step the event refers to
# - type: is the type of event that happened, as described below
#
def wizard_handler(params):
    '''
    General function to react to changes of the wizard step.
    This can be used to perform action when initializing or commiting a wizard step.
    '''

    print(f'Step {params["step"]}: {params["type"]}')

    #
    # Typically we would first filter by the step
    #
    if params["step"] == INITIAL_STEP:
        #
        # And then we would filter by event type.
        # Not all types need to be considered for every step of course.
        #
        if params["type"] == "initialized":
            #
            # A new step has been reached.
            #
            # Do setup for the new wizard step here, e.g. change the selection.
            #
            pass
        elif params["type"] == "discarded":
            #
            # The current step has been discarded, either by the user navigating to the previous step or aborting the whole dialog.
            # In the latter case a 'discarded' event for all previously completed steps will be emitted in reversed order.
            #
            # Do cleanup here, e.g., delete temporary elements or restore some selection.
            #
            pass
        elif params["type"] == "committed":
            #
            # The current step has been committed by the user.
            #
            # Finalize actions relevant to the step, e.g., create some (intermediate) element based on the current Dialog parameters.
            #
            pass
        elif params["type"] == "skipped":
            #
            # The current step has skipped by the user.
            #
            # This can also be used to clean up, which may or may not be the same as for the discarded event.
            #
            pass
        elif params["type"] == "branched":
            #
            # The user has pressed the branch button.
            #
            # This may be the same as the committed event, but it may also trigger a different action especially if there is no branch id set.
            #
            pass
        elif params["type"] == "id_changed":
            #
            # This is a general event when a the wizard step changes.
            # This can be reacted to in place of the more detailed events above, e.g., if only the current id is needed to adjust your workflow.
            #
            pass

    #
    # We can also check the step and type together.
    # In this case we handle the branch button on the final step to go directly to the label wizard in the Workflow Assistant.
    # However we need to first close the dialog so that it is successfully finished instead of aborted when the Workflow Assistant page changes.
    #
    if params["step"] == FINAL_STEP and params["type"] == "branched":
        gom.script.sys.close_user_defined_dialog(dialog=DIALOG)
        gom.script.sys.select_assistant_page(page="label_wizard", origin="d11d40a2-ede6-4085-b6d1-cf6be0335d0e")


DIALOG.wizard.handler = wizard_handler


#
# Finally we show the dialog. This will be displayed embedded in the Workflow Assistant, if this script is started by a EmbeddedCommandPage.
#
try:
    RESULT = gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    #
    # Instead of the committed event of a final step we can also do a resulting action after this function exits.
    # RESULT contains the value of every widget.
    #
except gom.BreakError as e:
    #
    # If the dialog is canceled, an exception is thrown and we can react to that here.
    #
    RESULT = 'Canceled!'

print('Result: ', RESULT)
