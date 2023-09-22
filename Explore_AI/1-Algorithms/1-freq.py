#!/usr/bin/python3

def find_freq(a, b):
    sorted_list = sorted(b)

    #initialize left side of the list index
    left_side = 0

    #initialize right side of the list index basically the end of the list
    right_side = len(sorted_list) - 1


    #the left side of the array should not be greater than the right
    while left_side <= right_side:
        #get midpoint of the list
        mid_point = (left + right) // 2

        mid_num = sorted_list[mid_point]

        if middle_element == a:
            #Target element found
            return middle_element
        elif middle_element < target:
            left_side = mid + 1
        else:
            right_side = mid - 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 4, 324, 564, 23, 45, 23, 54, 23, 54, 3, 56, 23, 6, 23, 435, 5, 2, 324, 56, 23, 56, 34, 123, 324]
target_element = 324
result = find_freq(target_element, my_list)

if result is not None:
    print(f"Element {target_element} found in the list.")
else:
    print(f"Element {target_element} not found in the list.")
