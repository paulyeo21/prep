import numpy

"""
The N Queen is the problem of placing N chess queens on an N x N
chessboard so that no two queens attack each other.
Queen attacks pieces on the same row, column, and diagonal
"""
class NQueens:
    def __init__(self, n):
        self.size = n
        self.grid = numpy.zeros((n, n))

    def legalMove(self, row, col):
        # Check if col has a queen
        for i in range(self.size):
            if self.grid[i][col] == 1:
                return False

        # Check top left diagonal
        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.grid[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check top right diagonal
        i = row
        j = col
        while i < self.size and j < self.size:
            if self.grid[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solveUtility(self, row, queens):
        if queens == 0:
            return True

        for i in range(self.size):
            # Check if queen can be placed on spot
            if self.legalMove(row, i):
                self.grid[row][i] = 1
                if self.solveUtility(row + 1, queens - 1):
                    return True
                # If not possible starting at this spot
                # Remove queen on this spot and continue iterating
                self.grid[row][i] = 0

        return False

    def solve(self):
        solution = self.solveUtility(0, self.size)
        if solution:
            print(self.grid)
            return solution

nqueens = NQueens(8)
print(nqueens.solve())
