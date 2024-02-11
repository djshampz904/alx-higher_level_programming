#!/usr/bin/python3
"""
Write a function that writes a string to a
text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text="", encoding="utf-8"):
    """
    Write a string to a text file
    """
    with open(filename, mode="w", encoding=encoding) as file:
        return file.write(text)
