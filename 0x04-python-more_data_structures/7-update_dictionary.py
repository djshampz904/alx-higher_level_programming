#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    found = False
    for mykey in a_dictionary:
        if key == mykey:
            a_dictionary[key] = value
            found = True
            break
    if not found:
        a_dictionary[key] = value

    return (a_dictionary)
