#!/usr/bin/python3
def uniq_add(my_list=[]):
    found = []
    sum = 0
    for item in my_list:
        is_found = False
        for i in found:
            if i == item:
                is_found = True
                break
        if not is_found:
            found.append(item)
            sum += item
    return (sum)
