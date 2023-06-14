#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """A function that computes the square value
       of all integers of a matrix

       Args:
        first arg: matrix

       Return: a new matrix of the same size as former
    """
    sqr_matrix = []

    for sett in matrix:
        lst = []
        for subset in sett:
            lst.append(subset ** 2)
        sqr_matrix.append(lst)
    return sqr_matrix
