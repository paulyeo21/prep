class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.links = [None] * 26

    def containsKey(self, char):
        return self.links[ord(char) - ord("a")] != None
    
    def get(self, char):
        return self.links[ord(char) - ord("a")]

    def put(self, char, node):
        self.links[ord(char) - ord("a")] = node

    def setEnd(self):
        self.isEnd = True

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        node = self.root
        for char in string:
            if not node.containsKey(char):
                node.put(char, TrieNode())
            node = node.get(char)
        node.setEnd()

    def search(self, string):
        current = self.root
        for char in string:
            current = current.get(char)
            if not current:
                return False

        if current.isEnd:
            return True
        else:
            return False
                

# trie = Trie()
# trie.insert("le")
# trie.insert("leet")
# print(trie.search("le"))
# print(trie.search("leet"))

