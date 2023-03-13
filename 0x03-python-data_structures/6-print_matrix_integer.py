#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        if x:
            print("{:d}".format(x[0]), end="")
            for y in x[1:]:
                print(" {:d}".format(y), end="")
        print("")
