import numpy as np
import sys

input = open("input.txt", "r")

grid = []
for line in input:
    row = list(line.strip())
    grid.append(row)

grid = np.array(grid)
print(grid.shape)

row,col = np.where(grid == '^')

while (row < 130 and row >= 0) and (col < 130 and col >= 0):
    if grid[row-1,col] == '#':
        grid = np.rot90(grid)
        row,col = np.where(grid == '^')
    grid[row,col] = 'X'
    row = row-1
    grid[row,col] = '^'

count = 0
for row in grid:
    for el in row:
        if el == 'X':
            count += 1

print(count)