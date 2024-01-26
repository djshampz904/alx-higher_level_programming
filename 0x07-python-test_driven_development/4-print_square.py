#!/bin/usr/python3
"""
This module contains a function that prints a square with the character #.
"""


def print_square(size):
    if size is None:
        raise TypeError("print_square() missing 1 required\
                        positional argument: 'size'")
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
