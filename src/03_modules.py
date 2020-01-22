"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
def print_the_args():
    for i in range(len(sys.argv)):
        print(sys.argv[i])

print_the_args()

# Print out the OS platform you're using:
# YOUR CODE HERE

def print_my_oper_sys():
    # Prints kernel, but not OS
    print(sys.platform)

print_my_oper_sys()

# Print out the version of Python you're using:
# YOUR CODE HERE

def print_pyth_vers():
    print(sys.version_info.major)

print_pyth_vers()

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

def print_current_pid():
    print(os.getpid())

print_current_pid()

# Print the current working directory (cwd):
# YOUR CODE HERE

def print_current_cwd():
    print(os.getcwd())

print_current_cwd()

# Print out your machine's login name
# YOUR CODE HERE

def print_current_user():
    print(os.getlogin())

print_current_user()