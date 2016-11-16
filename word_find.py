# import numpy

class WordFind:
    def findWords(self, grid, wordList):
        cols = len(grid)
        rows = len(grid[0])
        adj_list = {}

        for col in range(cols):
            for row in range(rows):
                char = grid[col][row]

                # Check down, right, down-right characters
                # If exist then create an edge in adj_list
                # Right
                if col + 1 < cols:
                    if char in adj_list:
                        adj_list[char] = grid[col + 1][row]
                    else:
                        adj_list[char] = {}

                # Down
                if row + 1 < rows:
                    adj_list[char] = grid[col][row + 1]

                # Down-right
                if col + 1 < cols and row + 1 < rows:
                    adj_list[char] = grid[col + 1][row + 1]

        print(adj_list)



wordFind = WordFind()
print(wordFind.findWords(["TEST", "GOAT", "BOAT"], ["GOAT", "BOAT", "TEST"])) # ["1 0", "2 0", "0 0"]
