#!/bin/usr/python3
"""
This module contains a function that adds two integers.
Default value of b is 98.
The function returns the sum of a and b.
"""


def add_integer(a, b=98):
    """
    This function adds two integers.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (a + b)
