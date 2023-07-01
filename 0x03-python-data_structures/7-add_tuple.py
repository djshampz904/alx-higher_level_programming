#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    element_1 = 0
    element_2 = 0
    if len(tuple_b) < 2 and len(tuple_b) == 0:
        pass
    else:
        element_1 = tuple_b[0]
    if len(tuple_b) >= 2:
        element_1 = tuple_b[0]
        element_2 = tuple_b[1]
    mytuple = (tuple_a[0] + element_1, tuple_a[1] + element_2)
    return mytuple
