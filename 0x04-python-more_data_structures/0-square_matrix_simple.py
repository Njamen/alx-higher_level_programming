#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    m = []
    for line in matrix:
        if line:
            m.append([x*x for x in line])
        else:
            m.append([])
    return m
