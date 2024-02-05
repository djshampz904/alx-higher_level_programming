#!/usr/bin/python3
"""
Class to check if an object is an instance of a class that
inherited from a specified class
"""


def inherits_from(obj, a_class):
    """
    Write a function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified class
    ; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
