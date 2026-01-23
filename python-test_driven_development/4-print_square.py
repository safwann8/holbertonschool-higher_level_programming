#!/usr/bin/python3
"""
print_square module.

This module includes a function that displays a square composed of '#'
characters according to a specified size.
"""


def print_square(size):
    """
    Outputs a square made of '#' characters.

    The size parameter determines both the width and height of the square.
    The function validates that size is a non-negative integer before printing.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
