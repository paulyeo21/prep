"""

If a dead cell has exactly 3 live neighbors, it'll be "born" in the next step.

If a live cell has <2 live neighbors, it'll die of lonliness in the next step
If a live cell has >3 live neighbors, it'll die of overcrowding in the next step

Otherwise, everything live stays live and everything dead stays dead.

..*..
..*..
..*..
.....

.....
.***.
.....
.....

..*..
..*..
..*..
.....

"""

def gameOfLife(board):
    if len(board[0]) > 0:
        new_board = [[None for x in range(len(board[0]))] for y in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                cell = board[row][col]
                live_neighbors = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        if row + x >= 0 and row + x < len(board) and col + y >= 0 and col + y < len(board[0]):
                            if board[row + x][col + y] == 1:
                                live_neighbors += 1
               # print "Row: ", row
               # print "Col: ", col
               # print "Cell: ", board[row][col]
               # print "Live neighbors: ", live_neighbors
                if cell:
                    if live_neighbors < 2:
                        new_board[row][col] = 0
                    elif live_neighbors > 3:
                        new_board[row][col] = 0
                    else:
                        new_board[row][col] = 1
                    
                else:
                    if live_neighbors == 3:
                        new_board[row][col] = 1
                    else:
                        new_board[row][col] = 0
               # print new_board
        return new_board
                
print(gameOfLife([[]]) == None)
print(gameOfLife([[0, 1],[0, 1]]) == [[0, 0],[0, 0]])
print(gameOfLife([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))# .*

