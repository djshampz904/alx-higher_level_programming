#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mydict = sorted(a_dictionary)
    for key in mydict:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
