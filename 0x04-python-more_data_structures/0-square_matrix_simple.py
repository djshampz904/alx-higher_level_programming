#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp = [row[:] for row in matrix]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp[i][j] = temp[i][j] * temp[i][j]
    return temp
