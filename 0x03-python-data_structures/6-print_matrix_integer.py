#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = 1
    for row in matrix:
        for number in row:
            if a % 3 != 0:
            print('{:d}'.format(number), end=" "])
        else:
             print('{:d}'.format(number), end="")
        print()

