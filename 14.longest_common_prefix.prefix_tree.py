class PrefixTreeNode:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTreeNode()
            node = node.children[c]
        
        node.endOfWord = True

    def longestCommonPrefix(self) -> str:
        prefix = ''
        node = self.root

        while len(node.children) == 1:
            if node.endOfWord:
                return prefix
            k = next(iter(node.children))
            prefix += k
            node = node.children[k]

        return prefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefixTree = PrefixTree()
        for s in strs:
            prefixTree.insert(s)
        
        return prefixTree.longestCommonPrefix()