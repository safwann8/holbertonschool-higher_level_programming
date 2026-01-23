#!/usr/bin/python3
"""
    Function that calculates the sum of two numbers.

    The parameters a and b must be integers or floating-point numbers.
    If a float is provided, it is converted to an integer before the addition.
"""
def add_integer(a, b=98):
    """
    Adds two values after validating their types.

    Both a and b must be integers or floats.
    Float values are converted to integers before being added together.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
