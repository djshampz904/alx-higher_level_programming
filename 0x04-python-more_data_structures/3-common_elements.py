#!/usr/bin/python3
def common_elements(set_1, set_2):
    len1 = len(set_1)
    len2 = len(set_2)
    found = []
    if len2 >= len1:
        for item in set_2:
            is_found = False
            for item2 in set_1:
                if item == item2:
                    is_found = True
                    found.append(item)
                    break
            if not is_found:
                continue
    elif len1 >= len2:
        for item in set_1:
            is_found = False
            for item2 in set_2:
                if item == item2:
                    is_found = True
                    found.append(item)
                    break
            if not is_found:
                continue
    return (found)
