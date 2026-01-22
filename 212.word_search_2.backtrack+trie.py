class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

class Solution:
    def findWords(self, board, words):
        
        trie = Trie()
        for word in words:
            trie.insert(word)

        m = len(board)
        n = len(board[0])
        visited = set()
        # Using a set because the same word can be found multiple times in the grid
        self.output = set()

        def dfs(i: int, j: int, word: str, node: TrieNode) -> bool:
            # Check all base conditions
            # We have found the word
            if node.word:
                self.output.add(word)
                # Do not return here as there can be a long word
            # Node has been previously visited
            if (i,j) in visited:
                return False
            # Index out of bound
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if board[i][j] in node.children:
                visited.add((i,j))
                child = node.children[board[i][j]]
                # even though it is not as readable, performance wise it is better to chain them in a long 
                # condition like this because if one succeeds then others won't have to be run unnecessarily
                if dfs(i+1, j, word+board[i][j], child) or dfs(i-1, j, word+board[i][j], child) or dfs(i, j+1, word+board[i][j], child) or dfs(i, j-1, word+board[i][j], child): return True
                # Backtrack
                visited.remove((i,j))
            return False
        
        for i in range(m):
            for j in range(n):
                visited = set()
                dfs(i,j,"", trie.root)
        
        return list(self.output)
