# Given 2x3 2d array representing a tic-tac-toe board,
# can you determine if you can win?
#
# Assume that you are "x" and that you are given a board and whose turn it is

def possibleToWin(board, myTurn):
    if hasWon(board, "x"):
        return True
    if hasWon(board, "o"):
        return False

    empty_coordinates = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ""):
                empty_coordinates.append((i, j))

    for x, y in empty_coordinates:
        if myTurn:
            board[x][y] = "x"
        else:
            board[x][y] = "o"
        if possibleToWin(board, not myTurn):
            return True

    return False

def hasWon(board, player):
    winning_states = \
        [[(0, 0), (1, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)]]
    for coordinates in winning_states:
        won = False
        for x, y in coordinates:
            if board[x][y] == player:
                won = True
            else:
                won = False
                break
        if won:
            return True
    return False

assert hasWon([["x", "o", "o"], ["x", "o", "o"], ["x", "", ""]], "x") == True
assert hasWon([["x", "o", "o"], ["x", "o", "o"], ["", "", ""]], "x") == False
assert possibleToWin([["x", "o", ""], ["x", "o", ""], ["", "", ""]], True) == True
assert possibleToWin([["x", "o", "x"], ["x", "o", "o"], ["o", "x", "o"]], True) == False
assert possibleToWin([["x", "o", "x"], ["x", "o", "o"], ["o", "", "o"]], False) == False
assert possibleToWin([["x", "o", "x"], ["x", "o", "x"], ["o", "", ""]], False) == False
assert possibleToWin([["x", "o", "x"], ["x", "o", "x"], ["o", "", ""]], True) == True

