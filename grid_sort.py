"""
Charlie has a grid of n rows by m columns. The rows are numbered 0 through n-1 from top to bottom. The columns are numbered 0 through m-1 from left to right.

Each cell of the grid contains a positive integer. The integers in Charlie's grid are a permutation of the numbers 1 through n*m. (I.e., each of these numbers occurs in the grid exactly once.)

Given a grid, its value list is a sequence constructed by listing all values in the grid in row major order. That is, we first list the values in row 0 from left to right, then the values in row 1 from left to right, and so on.

You are given the s n and m: the dimensions of Charlie's grid. You are also given a grid: the value list for Charlie's grid. (Formally, grid[i*m+j] is the value stored in row i, column j of the grid.)

Charlie can modify his grid in two ways: He may swap any two rows, and he may swap any two columns. Charlie now wonders whether there is a sequence of swaps that would sort his grid - that is, rearrange its elements in such a way that the value list of the new grid will be the ordered sequence (1,2,3,...,n*m).

If it is possible to sort Charlie's grid, return "Possible". Otherwise, return "Impossible".
"""
class GridSort:
    def sort(self, n, m, grid):
        # For rows (x - 1 because starts at 1..x)
        for i in range(n):
            current_row = (grid[i * m] - 1) / m
            for j in range(i * m + 1, i * m + m):
                comparison = (grid[j] - 1) / m
                if current_row != comparison:
                    return "Impossible"

        # For cols
        for i in range(m):
            current_col = (grid[i] - 1) % m
            for j in range(1, n):
                comparison = (grid[i + m * j] - 1) % m
                if current_col != comparison:
                    return "Impossible"

        return "Possible"

grid_sort = GridSort()
print(grid_sort.sort(2, 2, ( 1, 2, 3, 4 )))
print(grid_sort.sort(2, 2, ( 4, 3, 1, 2 )))
print(grid_sort.sort(3, 5, ( 10,6,8,9,7,5,1,3,4,2,15,11,13,14,12 )))
