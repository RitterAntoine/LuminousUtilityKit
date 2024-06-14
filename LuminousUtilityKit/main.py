import sys
from LuminousUtilityKit.src.printer import *
from LuminousUtilityKit.src.convertions import *
from LuminousUtilityKit.src.simulation.simulation import simulation

# List of functions that can be called
functions = {
    "print": ["hello_world", "hello", "print"],
    "convert": ["convert"],
    "simulation": ["simulation"]
}

def print_categories(args):
    if args[1] == functions["print"][0]:
        hello_world()
    elif args[1] == functions["print"][1]:
        hello(args[2])
    elif args[1] == functions["print"][2]:
        print(args[2])

def convertions_categories(args):
    value = float(args[2])
    from_unit = args[3]
    to_unit = args[4]

    try:
        result = convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(e)

def evolution_categories(args):
    if args[1] == functions["simulation"][0]:
        simulation()

# main function
def main():
    # Get all the arguments passed to the script
    args = sys.argv

    if len(args) == 1:
        help()
        return
    
    function_name = args[1]
    
    if function_name in functions["print"]:
        print_categories(args)
    elif function_name in functions["convert"]:
        convertions_categories(args)
    elif function_name in functions["simulation"]:
        evolution_categories(args)

if __name__ == "__main__":
    main()
