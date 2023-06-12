#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in range(len(matrix)):
        for g in range(len(matrix[g])):
            print('{:d}'.format(matrix[l][g]), end=''])
            if i < (len(matrix[l]) - 1):
                print(' ', end="")
            print()

