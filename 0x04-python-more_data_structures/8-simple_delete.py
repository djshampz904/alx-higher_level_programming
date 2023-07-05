#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == "":
        return (a_dictionary)
    key_to_remove = []

    for mykey in a_dictionary:
        if key == mykey:
            key_to_remove.append(mykey)

    for mykey in key_to_remove:
        del a_dictionary[mykey]

    return (a_dictionary)
