class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        def dfs(i, node):
            if i == len(s):
                return True
            if s[i] not in node.children:
                return False
            node = node.children[s[i]]
            if node.endOfWord:
                if dfs(i+1, trie.root):
                    return True
            return dfs(i+1, node)

        return dfs(0, trie.root)