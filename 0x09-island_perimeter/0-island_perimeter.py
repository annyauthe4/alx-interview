#!/usr/bin/python3
"""This module contains a function that returns the perimeter of the island
described in grid.
Grid is a list of list of integers.
0 represents water
1 represents land
Each cell is square with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t
connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid."""
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides
                perimeter += 4

                # Subtract sides that are shared with land neighbors
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # shared with top neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # shared with left neighbor

    return perimeter
