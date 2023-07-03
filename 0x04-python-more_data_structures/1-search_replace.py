#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp = [item for item in my_list]
    for i in range(len(temp)):
        if temp[i] == search:
            temp[i] = replace
        else:
            continue
    return (temp)
