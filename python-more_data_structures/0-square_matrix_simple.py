#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    return [[x ** 2 for x in row] for row in matrix]
