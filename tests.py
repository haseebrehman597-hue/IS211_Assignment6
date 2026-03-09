import unittest

from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit,
)
from conversions_refactored import convert, ConversionNotPossible


class TestConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        test_cases = [
            (300.00, 573.15),
            (0.00, 273.15),
            (-273.15, 0.00),
            (100.00, 373.15),
            (25.00, 298.15),
        ]

        for celsius, expected in test_cases:
            with self.subTest(celsius=celsius):
                print(f"Testing convertCelsiusToKelvin({celsius}) -> {expected}")
                self.assertAlmostEqual(convertCelsiusToKelvin(celsius), expected, places=2)

    def test_convertCelsiusToFahrenheit(self):
        test_cases = [
            (300.00, 572.00),
            (0.00, 32.00),
            (-40.00, -40.00),
            (100.00, 212.00),
            (25.00, 77.00),
        ]

        for celsius, expected in test_cases:
            with self.subTest(celsius=celsius):
                print(f"Testing convertCelsiusToFahrenheit({celsius}) -> {expected}")
                self.assertAlmostEqual(convertCelsiusToFahrenheit(celsius), expected, places=2)

    def test_convertFahrenheitToCelsius(self):
        test_cases = [
            (32.00, 0.00),
            (212.00, 100.00),
            (-40.00, -40.00),
            (572.00, 300.00),
            (77.00, 25.00),
        ]

        for fahrenheit, expected in test_cases:
            with self.subTest(fahrenheit=fahrenheit):
                print(f"Testing convertFahrenheitToCelsius({fahrenheit}) -> {expected}")
                self.assertAlmostEqual(convertFahrenheitToCelsius(fahrenheit), expected, places=2)

    def test_convertFahrenheitToKelvin(self):
        test_cases = [
            (32.00, 273.15),
            (212.00, 373.15),
            (-459.67, 0.00),
            (572.00, 573.15),
            (77.00, 298.15),
        ]

        for fahrenheit, expected in test_cases:
            with self.subTest(fahrenheit=fahrenheit):
                print(f"Testing convertFahrenheitToKelvin({fahrenheit}) -> {expected}")
                self.assertAlmostEqual(convertFahrenheitToKelvin(fahrenheit), expected, places=2)

    def test_convertKelvinToCelsius(self):
        test_cases = [
            (273.15, 0.00),
            (373.15, 100.00),
            (0.00, -273.15),
            (573.15, 300.00),
            (298.15, 25.00),
        ]

        for kelvin, expected in test_cases:
            with self.subTest(kelvin=kelvin):
                print(f"Testing convertKelvinToCelsius({kelvin}) -> {expected}")
                self.assertAlmostEqual(convertKelvinToCelsius(kelvin), expected, places=2)

    def test_convertKelvinToFahrenheit(self):
        test_cases = [
            (273.15, 32.00),
            (373.15, 212.00),
            (0.00, -459.67),
            (573.15, 572.00),
            (298.15, 77.00),
        ]

        for kelvin, expected in test_cases:
            with self.subTest(kelvin=kelvin):
                print(f"Testing convertKelvinToFahrenheit({kelvin}) -> {expected}")
                self.assertAlmostEqual(convertKelvinToFahrenheit(kelvin), expected, places=2)

    def test_refactored_temperature_conversions(self):
        test_cases = [
            ("Celsius", "Fahrenheit", 100.0, 212.0),
            ("Celsius", "Kelvin", 0.0, 273.15),
            ("Fahrenheit", "Celsius", 32.0, 0.0),
            ("Fahrenheit", "Kelvin", 212.0, 373.15),
            ("Kelvin", "Celsius", 273.15, 0.0),
            ("Kelvin", "Fahrenheit", 373.15, 212.0),
        ]

        for from_unit, to_unit, value, expected in test_cases:
            with self.subTest(from_unit=from_unit, to_unit=to_unit, value=value):
                print(f"Testing convert({from_unit}, {to_unit}, {value}) -> {expected}")
                self.assertAlmostEqual(convert(from_unit, to_unit, value), expected, places=2)

    def test_refactored_distance_conversions(self):
        test_cases = [
            ("Miles", "Meters", 1.0, 1609.344),
            ("Miles", "Yards", 1.0, 1760.0),
            ("Yards", "Meters", 1.0, 0.9144),
            ("Yards", "Miles", 1760.0, 1.0),
            ("Meters", "Miles", 1609.344, 1.0),
            ("Meters", "Yards", 0.9144, 1.0),
        ]

        for from_unit, to_unit, value, expected in test_cases:
            with self.subTest(from_unit=from_unit, to_unit=to_unit, value=value):
                print(f"Testing convert({from_unit}, {to_unit}, {value}) -> {expected}")
                self.assertAlmostEqual(convert(from_unit, to_unit, value), expected, places=3)

    def test_same_unit_returns_same_value(self):
        test_cases = [
            ("Celsius", "Celsius", 25.0),
            ("Fahrenheit", "Fahrenheit", 77.0),
            ("Kelvin", "Kelvin", 300.0),
            ("Miles", "Miles", 5.0),
            ("Yards", "Yards", 10.0),
            ("Meters", "Meters", 100.0),
        ]

        for from_unit, to_unit, value in test_cases:
            with self.subTest(from_unit=from_unit, to_unit=to_unit, value=value):
                print(f"Testing convert({from_unit}, {to_unit}, {value}) -> {value}")
                self.assertEqual(convert(from_unit, to_unit, value), value)

    def test_incompatible_units_raise_exception(self):
        test_cases = [
            ("Celsius", "Meters", 100.0),
            ("Miles", "Kelvin", 1.0),
            ("Yards", "Fahrenheit", 10.0),
        ]

        for from_unit, to_unit, value in test_cases:
            with self.subTest(from_unit=from_unit, to_unit=to_unit, value=value):
                print(f"Testing convert({from_unit}, {to_unit}, {value}) raises ConversionNotPossible")
                with self.assertRaises(ConversionNotPossible):
                    convert(from_unit, to_unit, value)


if __name__ == "__main__":
    unittest.main(verbosity=2)