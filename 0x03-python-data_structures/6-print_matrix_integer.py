#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integers."""

    for eset in matrix:
        for sset in eset:
            print("{:d}".format(sset), end=" " if sset != eset[-1] else "")
        print()
