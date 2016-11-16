from trie import Trie

def wordSearch(board, words):
    # 1. Iterate vertically and horizontally across board to insert into trie
    # 2. Iterate words to find if exists in trie

    trie = Trie()
    # Row wise
    for row in board:
        for i in range(1, len(row)):
            trie.insert("".join(row[:i+1]))

    # Column wise
    for row in range(len(board[0])):
        string = board[row][0]
        for col in range(1, len(board)):
            string += board[col][row]
            trie.insert(string)

    output = []
    for word in words:
        print(trie.search(word))
        if trie.search(word):
            output.append(word)

    return output

graph = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
print(wordSearch(graph, ["oath", "pea", "eat", "rain"]))
