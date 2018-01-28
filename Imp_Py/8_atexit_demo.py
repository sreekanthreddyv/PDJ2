# The atexit module provides a simple interface to register functions to
# be called when a program closes down normally.

import atexit
import sys


def all_done():
    print("All program finished")


def abc(a, b):
    print(a, b)
    # raise IndexError

atexit.register(all_done)
abc("Hacker", "Online")

# It is also possible to register more than one function, and to pass
# arguments. That can be useful to cleanly disconnect from databases,
# remove temporary files etc...

# Passing arguments to atexit function
def my_cleanup(name):
	print("my_cleanup(%s)" %name)

# atexit.register(my_cleanup, "first")
# atexit.register(my_cleanup, "Second")
# atexit.register(my_cleanup, "Third")

import os
import signal
import subprocess as sp
import time

proc = sp.Popen('2_ex_call.py')
print("PARENT: Pausing before sending signal...")
time.sleep(1)
print("PARENT: Signaling Child")
os.kill(proc.pid, signal.SIGTERM)