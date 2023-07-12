#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """A function that returns a list of lists of integers
       representing the Pascal’s triangle of n

       Args:
        n (int): is the number
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            prev_row = triangle[i - 1]
            value = prev_row[j - 1] + prev_row[j]
            row.append(value)

        row.append(1)

        triangle.append(row)

    return triangle
