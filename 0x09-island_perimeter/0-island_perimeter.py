#!/usr/bin/python3

""" Function to find perimiter of an island """


def island_perimeter(grid):
    """Find perimeter of an island"""
    perimeter = 0
    num_rows, num_cols = len(grid), len(grid[0])

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col]:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = row + dx, col + dy
                    if x < 0 or x >= num_rows or y < 0 or y >= num_cols or not grid[x][y]:
                        perimeter += 1

    return perimeter
