#!/usr/bin/python3
"""
3-say_my_name module.

This module contains a function that outputs a full name in a specific format.
It checks that the provided arguments are strings before printing the message.
"""


def say_my_name(first_name, last_name=""):
    """
    Displays a message with the given first and last names.

    The function verifies that both first_name and last_name are strings
    before printing them in the required format.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
