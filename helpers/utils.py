# This file contains utility functions that are used in the project.

#---------------------------------------------------------------------------
#   Imports
#---------------------------------------------------------------------------
#
# Here we import the modules we need for the script.
# The modules are located in the same folder as this script.
#
import random
import time


# --------------------------------------------------
# Delay between requests
# --------------------------------------------------
#
# This function is used to delay the requests to the github api.
# It is used to prevent getting blocked by the github api.
# The delay is a random number between 60 and 65 seconds.
#

def delay_between_requests() -> None:
    time.sleep(random.choice(list(range(60, 65))))