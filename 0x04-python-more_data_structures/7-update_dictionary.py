#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for mykey in a_dictionary:
        found = False
        if key == mykey:
            a_dictionary[key] = value
            found = True
    if not found:
        a_dictionary[key] = value

    return (a_dictionary)
