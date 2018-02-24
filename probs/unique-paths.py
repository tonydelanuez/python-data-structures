"""
Unique Paths

A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom right corner of the grid
- how many possible unique paths are there?
"""

def unique_paths(m, n):
    grid = [[0 for x in range(n+1)] for y in range(m+1)]
    grid[m - 1][n] = 1
    r = m - 1
    while(r >= 0):
        c = n - 1
        while(c >= 0):
            grid[r][c] = grid[r + 1][c] + grid[r][c + 1]
            c -= 1
        r -= 1
    for row in grid:
        print(row)
    return grid[0][0]

print(unique_paths(3, 7))
