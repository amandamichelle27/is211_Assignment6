# This structure maps SI units to dictionaries that map units to a pair (N, K)
# such that that unit can be converted to the SI equivalent by first being
# multiplied by N and then offset by K.
ratios = {
    "meter": {
        "mile":  (1609.34, 0),
        "yard":  (0.9144, 0),
    },
    "celsius": {
        "fahrenheit": (5.0 / 9.0, -160.0 / 9.0),
        "kelvin":     (1, -273.15),
    },
}

class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    # Identity conversion.
    if fromUnit == toUnit:
        return value

    # We are converting to SI, so we can use the given formula.
    if toUnit in ratios:
        if fromUnit in ratios[toUnit]:
            coef, offset = ratios[toUnit][fromUnit]
            return coef * value + offset
        else:
            raise ConversionNotPossible()
    # We are converting from SI, so just inverse the given formula.
    elif fromUnit in ratios:
        if toUnit in ratios[fromUnit]:
            coef, offset = ratios[fromUnit][toUnit]
            return (value - offset) / coef
        else:
            raise ConversionNotPossible()
    # Neither unit is SI.
    else:
        # Look for unit class that includes both and do both of the above.
        for unit, map in ratios.iteritems():
            if toUnit in map and fromUnit in map:
                (f_coef, f_offset), (t_coef, t_offset) = map[fromUnit], map[toUnit]
                return (f_coef * value + f_offset - t_offset) / t_coef
        # No common unit class was found.
        raise ConversionNotPossible()           