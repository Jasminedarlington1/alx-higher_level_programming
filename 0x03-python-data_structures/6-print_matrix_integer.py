#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = 1
    for row in matrix:
        for s in row:
            if a % 3 != 0:
            print('{:d}'.format(s), end=" "])
        else:
             print('{:d}'.format(s), end="")
             1 += 1
        print()

