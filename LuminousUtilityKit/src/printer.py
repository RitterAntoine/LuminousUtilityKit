# Function to print the message "Hello, World!"
def hello_world():
    print("Hello, World!")

# Function to print the message "Hello, <name>!"
def hello(name):
    print(f"Hello, {name}!")

def welcome():
    print("Welcome to the Luminous Utility Kit!")
    print("Type 'LuminousUtilityKit.exe help' to see the available functions")

def help():
    print("")
    print("The goal of this project is to develop a bunch of functions that will be called in a terminal")
    print("The functions will be called with the following syntax:")
    print("LuminousUtilityKit.exe <function_name> <arguments>")
    print("The following functions are available:")
    print("hello_world")
    print("hello <name>")
    print("print <message>")
    print("convert <value> <unit_1> <unit_2>")
    print("bacteria_simulation")
    print("life_simulation")