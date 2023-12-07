#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    arr = []
    for row in matrix:
        sub_matrix = map(lambda num: num**2, row)
        arr.append(list(sub_matrix))
    return arr
