"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""
def islandPerimeter(grid):
    perimeter = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            current = grid[x][y]
            if current == 1:
                # Left
                if x - 1 < 0 or grid[x - 1][y] == 0:
                    perimeter += 1
                # Right
                if x + 1 >= len(grid[0]) or grid[x + 1][y] == 0:
                    perimeter += 1
                # Down
                if y - 1 < 0 or grid[x][y - 1] == 0:
                    perimeter += 1
                # Up
                if y + 1 >= len(grid) or grid[x][y + 1] == 0:
                    perimeter += 1
            
    return perimeter

grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeter(grid))

