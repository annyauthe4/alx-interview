#!/usr/bin/python3
"""This module calculates the fewest number of operations needed
to result in exactly n number of a character in a file.
"""


def minOperations(n):
    """Returns minimum num of operations."""
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
