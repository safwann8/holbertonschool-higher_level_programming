#!/usr/bin/python3
"""
text_indentation module.

This module provides a function that formats and prints a text.
It inserts two line breaks after each '.', '?' or ':' character
and ensures that no line starts or ends with extra spaces.
"""


def text_indentation(text):
    """
    Displays a formatted version of the given text.

    The function prints the text while adding two new lines after
    each '.', '?' or ':' character. Leading spaces at the beginning
    of each printed line are ignored.

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: If the provided argument is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    at_line_start = True

    for c in text:
        if at_line_start and c == " ":
            continue

        line += c
        at_line_start = False

        if c in ".?:":
            print(line.rstrip(" "))
            print()
            line = ""
            at_line_start = True

    line = line.strip(" ")
    if line != "":
        print(line, end="")
