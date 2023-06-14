#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return (list(map(lambda new_matrix: [i ** 2 for i in new_matrix], matrix)))
