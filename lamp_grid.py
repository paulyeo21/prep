"""
Given an NxN grid with an array of lamp coordinates. Each lamp provides illumination 
to every square on their x axis, every square on their y axis, and every square that 
lies in their diagonal (think of a Queen in chess). Given an array of query coordinates, 
determine whether that point is illuminated or not. The catch is when checking a query 
all lamps adjacent to, or on, that query get turned off. The ranges for the variables/arrays 
were about: 10^3 < N < 10^9, 10^3 < lamps < 10^9, 10^3 < queries < 10^9.  
"""
class LampGrid:
    def __init__(self, size, lamps):
        self.size = size
        self.grid = [[0 for x in range(size)] for y in range(size)]
        self.illuminateBoard(lamps)

    def illuminateBoard(self, lamps):
        for x, y in lamps:
            self.grid[x][y] = 1

    def isIlluminated(self, coordinate, grid):
        x = coordinate[0]
        y = coordinate[1]

        # Rows
        for i in range(self.size):
            if grid[i][y] == 1:
                return False

        # Cols
        for i in range(self.size):
            if grid[x][i] == 1:
                return False
        
        # Diagonals
        i = x
        j = y
        while i >= 0 and j >= 0:
            if grid[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i = x
        j = y
        while i >= 0 and j < self.size:
            if grid[i][j] == 1:
                return False
            i -= 1
            j += 1

        i = x
        j = y
        while i < self.size and j < self.size:
            if grid[i][j] == 1:
                return False
            i += 1
            j += 1

        i = x
        j = y
        while i < self.size and j >= 0:
            if grid[i][j] == 1:
                return False
            i += 1
            j -= 1
            
        return True

    def concealedBoard(self, coordinate):
        grid = self.grid
        x = coordinate[0]
        y = coordinate[1]

        # On row
        for i in range(-1, 2):
            if x + i >= 0 and x + i < self.size and y >= 0 and y < self.size:
                grid[x + i][y] = 0

        # On col
        for i in range(-1, 2):
            if x >= 0 and x < self.size and y + i >= 0 and y + i < self.size:
                grid[x][y + i] = 0

        # Diagonals
        for i in range(-1, 2):
            if x + i >= 0 and x + i < self.size and y + i >= 0 and y + i < self.size:
                grid[x + i][y + i] = 0
            if x - i >= 0 and x - i < self.size and y + i >= 0 and y + i < self.size:
                grid[x - i][y + i] = 0
            if x + i >= 0 and x + i < self.size and y - i >= 0 and y - i < self.size:
                grid[x + i][y - i] = 0
            if x - i >= 0 and x - i < self.size and y - i >= 0 and y - i < self.size:
                grid[x - i][y - i] = 0
        
        return self.isIlluminated(coordinate, grid)

    def solution(self, queries):
        output = []
        for x, y in queries:
            output.append(self.concealedBoard((x, y)))
        return output

lamp_grid = LampGrid(4, [(1, 0), (0, 2), (2, 3)])
print(lamp_grid.solution([(0, 0), (0, 1), (3, 1)]))

