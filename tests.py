#!/usr/bin/python2.7

# Standard Library Imports
from unittest import main, TestCase

# Local Imports
from conversions import convertCelsiusToFahrenheit
from conversions import convertCelsiusToKelvin
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvinToCelsius
from conversions import convertKelvinToFahrenheit
from conversions_refactored import ConversionNotPossible, convert


class TestConv(TestCase):
    def test_convertCelsiusToFahrenheit(self):
        cases = {
            -40: -40,
            0:   32,
            50:  122,
            100: 212,
            123: 253.4,
        }
        for input, output in cases.iteritems():
            print "input (C):", input, "expected output (F):", output
            self.assertAlmostEqual(convertCelsiusToFahrenheit(input), output, 2)
            self.assertAlmostEqual(convert("celsius", "fahrenheit", input), output, 2)

    def test_convertCelsiusToKelvin(self):
        cases = {
            -273.15: 0,
            0:       273.15,
            50:      323.15,
            100:     373.15,
            200:     473.15,
        }
        for input, output in cases.iteritems():
            print "input (C):", input, "expected output (K):", output
            self.assertAlmostEqual(convertCelsiusToKelvin(input), output, 2)
            self.assertAlmostEqual(convert("celsius", "kelvin", input), output, 2)

    def test_convertFahrenheitToCelsius(self):
        cases = {
            -40: -40,
            32:  0,
            50:  10,
            95:  35,
            212: 100,
        }
        for input, output in cases.iteritems():
            print "input (F):", input, "expected output (C):", output
            self.assertAlmostEqual(convertFahrenheitToCelsius(input), output, 2)
            self.assertAlmostEqual(convert("fahrenheit", "celsius", input), output, 2)

    def test_convertFahrenheitToKelvin(self):
        cases = {
            32:  273.15,
            0:   255.37,
            50:  283.15,
            100: 310.93,
            123: 323.71,
        }
        for input, output in cases.iteritems():
            print "input (F):", input, "expected output (K):", output
            self.assertAlmostEqual(convertFahrenheitToKelvin(input), output, 2)
            self.assertAlmostEqual(convert("fahrenheit", "kelvin", input), output, 2)

    def test_convertKelvinToCelsius(self):
        cases = {
            -40: -313.15,
            0:   -273.15,
            50:  -223.15,
            100: -173.15,
            123: -150.15,
        }
        for input, output in cases.iteritems():
            print "input (K):", input, "expected output (C):", output
            self.assertAlmostEqual(convertKelvinToCelsius(input), output, 2)
            self.assertAlmostEqual(convert("kelvin", "celsius", input), output, 2)

    def test_convertKelvinToFahrenheit(self):
        cases = {
            -40: -531.67,
            0:   -459.67,
            50:  -369.67,
            100: -279.67,
            123: -238.27,
        }
        for input, output in cases.iteritems():
            print "input (K):", input, "expected output (F):", output
            self.assertAlmostEqual(convertKelvinToFahrenheit(input), output, 2)
            self.assertAlmostEqual(convert("kelvin", "fahrenheit", input), output, 2)

    def test_convertLength(self):
        cases = [
            ("mile", "yard", 1, 1760),
            ("mile", "meter", 1, 1609.34),
            ("yard", "meter", 1, 0.9144),
            ("yard", "mile", 1760, 1),
            ("meter", "yard", 1, 1.09361),
            ("meter", "mile", 1600, 0.9941),
        ]
        for fromUnit, toUnit, input, output in cases:
            print "input:", input, fromUnit, "\texpected output:", output, toUnit
            self.assertAlmostEqual(convert(fromUnit, toUnit, input), output, 2)

    def test_convertIdentity(self):
        cases = [
            ("mile", "mile", 1, 1),
            ("meter", "meter", 1, 1),
            ("yard", "yard", 1, 1),
            ("celsius", "celsius", 1, 1),
            ("fahrenheit", "fahrenheit", 1, 1),
            ("kelvin", "kelvin", 1, 1),
        ]
        for fromUnit, toUnit, input, output in cases:
            print "input:", input, fromUnit, "\texpected output:", output, toUnit
            self.assertAlmostEqual(convert(fromUnit, toUnit, input), output, 2)
            
    def test_convertIncompatible(self):
        self.assertRaises(ConversionNotPossible, convert, "mile", "celsius", 1)

if __name__ == "__main__":
    main()
