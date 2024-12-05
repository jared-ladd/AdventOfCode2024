import numpy as np

input = open("input.txt", "r")

grid = []
for line in input:
    row = list(line)
    row.pop() # remove newline
    grid.append(row)

grid = np.array(grid)

# count occurances of 'XMAS'
def countLine(line):
    l,r = 0,3
    res = 0
    while r < len(line):
        word = "".join(line[l:r+1])
        res += 1 if word == "XMAS" else 0
        l += 1
        r += 1

    return res

def countGrid(grid):
    count = 0
    for line in grid:
        count += countLine(line)
    return count

def countDiagonal(grid):
    count = 0
    for i in range(-136, 137):
        diagonal = np.diag(grid, k=i)
        count += countLine(diagonal)
    return count

def is_X_of_MAS(grid):
    potentialMAS1 = "".join(np.diag(grid))
    potentialMAS2 = "".join(np.diag(np.rot90(grid)))
    MAS1_exists = potentialMAS1 == "MAS" or potentialMAS1 == "SAM"
    MAS2_exists = potentialMAS2 == "MAS" or potentialMAS2 == "SAM"
    return MAS1_exists and MAS2_exists
        
part1count = 0
part1count += countGrid(grid)
part1count += countDiagonal(grid)

grid_90 = np.rot90(grid)
part1count += countGrid(grid_90)
part1count += countDiagonal(grid_90)

grid_180 = np.rot90(grid_90)
part1count += countGrid(grid_180)
part1count += countDiagonal(grid_180)

grid_270 = np.rot90(grid_180)
part1count += countGrid(grid_270)
part1count += countDiagonal(grid_270)

print(f'Part 1 count: {part1count}')

part2count = 0
for i in range(1, 139):
    for j in range(1, 139):
        potentialX = grid[i-1:i+2,j-1:j+2]
        part2count += 1 if is_X_of_MAS(potentialX) else 0

print(part2count)
        