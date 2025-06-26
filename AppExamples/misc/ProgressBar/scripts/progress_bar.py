# -*- coding: utf-8 -*-
#
# progress_bar.py
#
# Example for controlling the progress bar in the ZEISS INSPECT main window
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import gom
import time
import gom.api.progress

# In this example, the progress bar is cancelled when the 'with' block is left
print("Showing progress bar until end of 'with' block is reached...", end="")
with gom.api.progress.ProgressBar() as bar:
    bar.set_message('Counting atoms in the universe... ')
    for i in range(100):
        # Pretend to be busy...
        time.sleep(0.1)
        # Increase the progress
        bar.set_progress(i)
    bar.set_message("Getting bored - stopping!")
    time.sleep(5)
print(" done!")

# In this example, the progress bar is cancelled by calling finish_progress() 
# while the 'with' block continues
print("Showing progress bar until finish_progress() is called...", end="")
with gom.api.progress.ProgressBar() as bar:
    bar.set_message('Counting coins in your pocket... ')
    for i in range(100):
        # Pretend to be busy...
        time.sleep(0.1)
        # Increase the progress
        bar.set_progress(i)
    bar.set_message("That's enough to buy a coffee - stopping for a coffee break!")
    time.sleep(5)
    # Remove progress bar
    bar.finish_progress()
    print(" stopped by finish_progress()!")
    time.sleep(10)
print("End of 'with' block reached.")
