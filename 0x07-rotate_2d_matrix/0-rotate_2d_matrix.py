#!/usr/bin/python3
"""
This module contains a function that rotates an n x n
matrices without using extra space.
"""


def rotate_2d_matrix(matrix):
    """Rotates matrix clockwisely by 90 degree."""
    n = len(matrix)

    # Transpose each:
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
