#!/usr/bin/python3
def best_score(a_dictionary):
    largest = 0
    if not a_dictionary:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > largest:
            largest = a_dictionary[key]

    return(largest)
