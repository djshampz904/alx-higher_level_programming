#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mydict = a_dictionary.copy()
    mykeys = []

    for key in mydict:
        mykeys.append(key)

    for key in mykeys:
        mydict[key] = mydict[key] * 2
    return (mydict)
