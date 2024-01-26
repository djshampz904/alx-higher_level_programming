#!/bin/usr/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix.
    """
    temp1 = []
    temp2 = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for i in matrix:
        """
        Clear temp1 for each iteration
        """
        temp1 = []
        if len(i) != len(matrix[0]):
            raise TypeError(
                "Each row of the matrix must have the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists)\
                    of integers/floats")
            temp1.append(round(j / div, 2))
        temp2.append(temp1)
    return temp2
