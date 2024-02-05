#!/usr/bin/python3
class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
