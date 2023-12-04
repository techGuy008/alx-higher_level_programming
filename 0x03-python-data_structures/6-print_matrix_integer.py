#!/usr/bin/python3
def print_matrix_integer(matrix1=[[]]):
    for row in matrix1:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
