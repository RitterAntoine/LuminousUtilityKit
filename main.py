# The goal of this project is to develop a bunch of functions that will be called in a terminal
# The functions will be called with the following syntax:
# python main.py <function_name> <arguments>

import sys
import printer
from printer import *

# main function
def main():
    # Get all the arguments passed to the script
    args = sys.argv

    # Check if the first argument is the name of the function to be called
    if args[1] == "hello_world":
        printer.hello_world()
    elif args[1] == "hello_name":
        printer.hello_name(args[2])

if __name__ == "__main__":
    main()