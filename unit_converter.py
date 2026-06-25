"""
Task 2: Unit Converter Tool
----------------------------
A command-line unit converter supporting Length, Weight, Temperature,
and Volume conversions.

Usage:
    python unit_converter.py
"""

# Conversion factors relative to a base unit for each category
LENGTH_UNITS = {
    "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
    "inch": 0.0254, "ft": 0.3048, "yard": 0.9144, "mile": 1609.34,
}

WEIGHT_UNITS = {
    "mg": 0.001, "g": 1.0, "kg": 1000.0, "ton": 1_000_000.0,
    "lb": 453.592, "oz": 28.3495,
}

VOLUME_UNITS = {
    "ml": 0.001, "l": 1.0, "gallon": 3.78541,
    "cup": 0.24, "pint": 0.473176, "quart": 0.946353,
}


def convert_linear(value: float, from_unit: str, to_unit: str, table: dict) -> float:
    """Generic conversion using a base-unit factor table."""
    if from_unit not in table or to_unit not in table:
        raise ValueError(f"Unknown unit. Available: {', '.join(table.keys())}")
    base_value = value * table[from_unit]
    return base_value / table[to_unit]


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    from_unit, to_unit = from_unit.lower(), to_unit.lower()
    valid = {"c", "f", "k", "celsius", "fahrenheit", "kelvin"}
    if from_unit not in valid or to_unit not in valid:
        raise ValueError("Available units: C, F, K")

    # Normalize
    aliases = {"celsius": "c", "fahrenheit": "f", "kelvin": "k"}
    from_unit = aliases.get(from_unit, from_unit)
    to_unit = aliases.get(to_unit, to_unit)

    # Convert input to Celsius first
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15

    # Convert Celsius to target
    if to_unit == "c":
        return celsius
    elif to_unit == "f":
        return celsius * 9 / 5 + 32
    elif to_unit == "k":
        return celsius + 273.15


def print_units(table: dict):
    print("Available units:", ", ".join(table.keys()))


def main():
    categories = {
        "1": ("Length", LENGTH_UNITS),
        "2": ("Weight", WEIGHT_UNITS),
        "3": ("Temperature", None),
        "4": ("Volume", VOLUME_UNITS),
    }

    while True:
        print("\n===== UNIT CONVERTER =====")
        for key, (name, _) in categories.items():
            print(f"{key}. {name}")
        print("5. Exit")

        choice = input("Choose a category: ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in categories:
            print("Invalid choice, try again.")
            continue

        name, table = categories[choice]

        try:
            if name == "Temperature":
                print("Units: C, F, K")
                from_unit = input("From unit: ").strip()
                to_unit = input("To unit: ").strip()
                value = float(input("Value: ").strip())
                result = convert_temperature(value, from_unit, to_unit)
            else:
                print_units(table)
                from_unit = input("From unit: ").strip().lower()
                to_unit = input("To unit: ").strip().lower()
                value = float(input("Value: ").strip())
                result = convert_linear(value, from_unit, to_unit, table)

            print(f"\nResult: {value} {from_unit} = {result:.4f} {to_unit}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
