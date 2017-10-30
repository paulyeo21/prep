"""
Given a sudoku board check if the board is solved.
"""

# board: nxn
def sudokuValidator(board):
    if not board: return False
    if len(board) != 9 or len(board[0]) != 9: return False

    # 1. Check each row if 1-9 are all represented
    # T: O(n) with assumption that checking is O(1)
    for row in board:
        if not areDigitsRepresented(row):
            return False

    # 2. Similarly check for column wise
    # T: O(n^2)
    for col in range(len(board)):
        column = []
        for row in range(len(board[0])):
            column.append(board[row][col])

        if not areDigitsRepresented(column):
            return False

    # 3. Iterate over 3x3 grids and same-- check if all 1-9 represented
    i = 0
    while i < len(board) / 3:
        j = 0
        while j < len(board[0]) / 3:
            grid = []
            for col in range(i * 3, (i + 1) * 3):
                for row in range(j * 3, (j + 1) * 3):
                    grid.append(board[row][col])

            if not areDigitsRepresented(column):
                return False
            j += 1
        i += 1

    return True

# T: O(n log n)
def areDigitsRepresented(digits):
    return sorted(digits) == [1,2,3,4,5,6,7,8,9]
         

board1 = [
  [5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]
]

board2 = []

board3 = [
  [5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,None]
]

board4 = [
  [5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5]
]

assert sudokuValidator(board1) == True
assert sudokuValidator(board2) == False
assert sudokuValidator(board3) == False
assert sudokuValidator(board4) == False

