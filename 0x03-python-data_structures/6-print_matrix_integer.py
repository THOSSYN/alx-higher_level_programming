#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integers."""

    for each_set in matrix:
        for sub_set in each_set:
            print("{:d}".format(sub_set), end=" " if sub_set != each_set[-1] else "")
        print()
