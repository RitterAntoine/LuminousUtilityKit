# The goal of this project is to develop a bunch of functions that will be called in a terminal
# The functions will be called with the following syntax:
# python main.py <function_name> <arguments>

import sys
import printer
from printer import *
import convertions
from convertions import *

# main function
def main():
    # Get all the arguments passed to the script
    args = sys.argv

    # Check if the first argument is the name of the function to be called
    if args[1] == "hello_world":
        printer.hello_world()
    elif args[1] == "hello_name":
        printer.hello_name(args[2])
    elif args[1] == "convert":
        value = float(args[2])
        unit_1 = args[3]
        unit_2 = args[4]
        if unit_1 == "km" and unit_2 == "miles":
            print(value, "km is equal to", convert_km_to_miles(value), "miles")
        elif unit_1 == "miles" and unit_2 == "km":
            print(value, "miles is equal to", convert_miles_to_km(value), "km")

if __name__ == "__main__":
    main()