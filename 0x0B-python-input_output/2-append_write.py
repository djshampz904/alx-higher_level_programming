#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text="", encoding="utf-8"):
    """Appends a string at the end of a text file (UTF8) and returns the
    number of characters added"""

    with open(filename, mode="a", encoding=encoding) as file:
        return file.write(text)
