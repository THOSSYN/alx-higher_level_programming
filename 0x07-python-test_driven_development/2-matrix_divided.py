#!/usr/bin/python3

def matrix_divided(matrix, div):
    """This function divides all elements of a matrix

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Raises:
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If matrix is not a matrix (list of lists) of integers/floats.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If an attempt is made to divide by 0.

    Returns:
        list: A new matrix with all elements divided by div and rounded to 2 decimal places.
    """
    nu_matrix = []

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        nu_row = []
        for element in row:
            nu_row.append(round(element / div, 2))
        nu_matrix.append(nu_row)

    return nu_matrix
