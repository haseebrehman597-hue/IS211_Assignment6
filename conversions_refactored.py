class ConversionNotPossible(Exception):
    pass


TEMPERATURE_UNITS = {"Celsius", "Fahrenheit", "Kelvin"}
DISTANCE_UNITS = {"Miles", "Yards", "Meters"}


def convert(fromUnit: str, toUnit: str, value: float) -> float:
    if fromUnit == toUnit:
        return float(value)

    if fromUnit in TEMPERATURE_UNITS and toUnit in TEMPERATURE_UNITS:
        return _convert_temperature(fromUnit, toUnit, value)

    if fromUnit in DISTANCE_UNITS and toUnit in DISTANCE_UNITS:
        return _convert_distance(fromUnit, toUnit, value)

    raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit}")


def _convert_temperature(fromUnit: str, toUnit: str, value: float) -> float:
    to_celsius = {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x - 32) * 5 / 9,
        "Kelvin": lambda x: x - 273.15,
    }

    from_celsius = {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9 / 5) + 32,
        "Kelvin": lambda x: x + 273.15,
    }

    celsius_value = to_celsius[fromUnit](value)
    return float(from_celsius[toUnit](celsius_value))


def _convert_distance(fromUnit: str, toUnit: str, value: float) -> float:
    to_meters = {
        "Meters": 1.0,
        "Yards": 0.9144,
        "Miles": 1609.344,
    }

    meters_value = value * to_meters[fromUnit]
    return float(meters_value / to_meters[toUnit])
