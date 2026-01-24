class Node:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False

class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        # Populate the tree
        root = Node()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.endOfWord = True
        
        # Search through text
        i = 0
        res = []
        for i in range(len(text)):
            node = root
            j = i
            while j < len(text) and text[j] in node.children:
                node = node.children[text[j]]
                if node.endOfWord:
                    res.append([i,j])
                j += 1

        return res