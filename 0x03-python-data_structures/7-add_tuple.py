#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    element_1a = 0
    element_2a = 0
    element_1b = 0
    element_2b = 0

    if len(tuple_b) < 2 and len(tuple_b) == 0:
        pass
    else:
        element_1b = tuple_b[0]
    if len(tuple_b) >= 2:
        element_1b = tuple_b[0]
        element_2b = tuple_b[1]

    if len(tuple_a) < 2 and len(tuple_a) == 0:
        pass
    else:
        element_1a = tuple_a[0]
    if len(tuple_a) >= 2:
        element_1a = tuple_a[0]
        element_2a = tuple_a[1]

    mytuple = (element_1a + element_1b, element_2a + element_2b)
    return mytuple
