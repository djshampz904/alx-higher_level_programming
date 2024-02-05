#!/usr/bin/python3
"""
This module returns the list of available attributes
"""

class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
