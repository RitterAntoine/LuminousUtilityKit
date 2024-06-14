# Define base units for different types of measurements
base_units = {
    'length': 'meters',
    'mass': 'kilograms',
    'time': 'seconds',
}

# Conversion factors to base units
to_base_factors = {
    'km': ('meters', 1000),
    'miles': ('meters', 1609.34),
    'meters': ('meters', 1),
    'feet': ('meters', 0.3048),
    'cm': ('meters', 0.01),
    'inches': ('meters', 0.0254),
    'mm': ('meters', 0.001),
    'yards': ('meters', 0.9144),
    'nautical_miles': ('meters', 1852),
    'furlongs': ('meters', 201.168),
    'light_years': ('meters', 9.461e15),
}

# Conversion factors from base units
from_base_factors = {
    'meters': {
        'km': 1 / 1000,
        'miles': 1 / 1609.34,
        'meters': 1,
        'feet': 1 / 0.3048,
        'cm': 1 / 0.01,
        'inches': 1 / 0.0254,
        'mm': 1 / 0.001,
        'yards': 1 / 0.9144,
        'nautical_miles': 1 / 1852,
        'furlongs': 1 / 201.168,
        'light_years': 1 / 9.461e15,
    },
}

def convert(value, from_unit, to_unit):
    if from_unit not in to_base_factors or to_unit not in from_base_factors['meters']:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported")

    # Convert from the original unit to the base unit
    base_unit, to_base_factor = to_base_factors[from_unit]
    base_value = value * to_base_factor

    # Convert from the base unit to the target unit
    from_base_factor = from_base_factors[base_unit][to_unit]
    return base_value * from_base_factor
