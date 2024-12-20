# Approach: Backtracking + Hash Set
# We need to use a set of "visited" nodes to prevent the algorithm from going backwards
# for example, ['A','B'] board should not return True for "ABA"
# Verdict: Pass

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()

        # i = index of character we are checking in word
        def dfs(i: int, j: int, k: int):
            if k == len(word):
                return True
            
            if (i,j) in visited:
                return False

            if 0 <= i < m and 0 <= j < n and board[i][j] == word[k]:
                visited.add((i,j))
                path1 = dfs(i+1, j, k+1)
                path2 = dfs(i-1, j, k+1)
                path3 = dfs(i, j+1, k+1)
                path4 = dfs(i, j-1, k+1)
                visited.remove((i,j)) # Backtrack
                return path1 or path2 or path3 or path4
            
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        
        return False