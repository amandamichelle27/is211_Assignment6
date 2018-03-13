#!/usr/bin/python2.7
 
def convertCelsiusToFahrenheit(degrees):
    return 1.8 * degrees + 32

def convertCelsiusToKelvin(degrees):
    return degrees + 273.15
    
def convertFahrenheitToCelsius(degrees):
    return 5.0 * (degrees - 32) / 9.0

def convertFahrenheitToKelvin(degrees):
    return 5.0 * (degrees - 32) / 9.0 + 273.15

def convertKelvinToCelsius(degrees):
    return degrees - 273.15
    
def convertKelvinToFahrenheit(degrees):
    return 1.8 * (degrees - 273.15) + 32

