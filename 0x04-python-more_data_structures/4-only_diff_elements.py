#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique = []
    for item in set_1:
        is_found = False
        for item2 in set_2:
            if item == item2:
                is_found = True
                break
        if not is_found:
            unique.append(item)
    for item in set_2:
        is_found = False
        for item2 in set_1:
            if item == item2:
                is_found = True
                break
        if not is_found:
            unique.append(item)
    return (unique)
