#!/usr/bin/python3
"""
This module contains a function which returns a list of lists
of integers representing the Pascal's triangle of n.
Where n is the number of rows in the triangle.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers."""
    if n <= 0:
        return []

    res = [[1]]

    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res


if __name__ == "__main__":
    pascal_triangle(n)
