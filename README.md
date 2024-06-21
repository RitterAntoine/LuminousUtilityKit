# Luminous Utility Kit

The Luminous Utility Kit is a Python library designed to offer a variety of utility functions for printing, conversions, and simulations. This README provides an overview of the project, how to install it, and examples of how to use the various functions available.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Printing Functions](#printing-functions)
  - [Conversion Functions](#conversion-functions)
  - [Simulation Functions](#simulation-functions)
- [Functions Overview](#functions-overview)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use the Luminous Utility Kit, you need to clone the repository and ensure you have Python installed.

```sh
git clone https://github.com/RitterAntoine/LuminousUtilityKit.git
cd LuminousUtilityKit
```
Make sure to install any required dependencies (if any) mentioned in the `requirements.txt` file.

```sh
pip install -r requirements.txt
```

You can also install the package in editable mode to allow running the script from anywhere on your system:

```sh
pip install -e .
```

## Usage

The `main.py` script serves as the entry point for the Luminous Utility Kit. Depending on the function you want to use, you can call the script with different arguments.

### Printing Functions

- `hello_world`: Prints "Hello, World!"
- `hello <name>`: Prints a greeting to the specified name.
- `print <message>`: Prints the specified message.

#### Example Usage:

```sh
LuminousUtilityKit.exe hello_world
LuminousUtilityKit.exe hello Alice
LuminousUtilityKit.exe print "This is a test message"
```

### Convertion Functions

- `convert <value> <from_unit> <to_unit>`: Converts a value from one unit to another.

#### Example Usage:

```sh
LuminousUtilityKit.exe convert 8 km miles
```

### Simulation Functions

- `bacteria_simulation`: Runs a bacteria growth simulation.
- `life_simulation`: Runs a life simulation.

#### Example Usage:

```sh
LuminousUtilityKit.exe bacteria_simulation
LuminousUtilityKit.exe life_simulation
```

## Functions Overview

The Luminous Utility Kit includes the following functions organized into categories:

### Printing Functions

- hello_world(): Prints "Hello, World!"
- hello(name: str): Prints a greeting to the specified name.
- print(message: str): Prints the specified message.

### Conversion Functions

- convert(value: float, from_unit: str, to_unit: str): Converts a value from one unit to another.

### Simulation Functions

- bacteria_simulation(): Runs a bacteria growth simulation.
- life_simulation(): Runs a life simulation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
