class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        assert(self.root)
        cur = self.root

        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]

        cur.endOfWord = True

    def search(self, word: str) -> bool:

        # j = index of current character in word
        def dfs(j, node) -> bool:

            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in node.children:
                        if child and dfs(i+1, child):
                            return True
                    return False
                else:
                    i = ord(c) - ord('a')
                    if node.children[i] is None:
                        return False
                    node = node.children[i]
            
            return node.endOfWord
            
        return dfs(0, self.root)