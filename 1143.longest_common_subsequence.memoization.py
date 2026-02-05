class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = dict()

        def dfs(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in self.memo:
                return self.memo[(i,j)]
            if text1[i] == text2[j]:
                self.memo[(i,j)] = 1 + dfs(i+1, j + 1)
            else:
                self.memo[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))
            return self.memo[(i,j)]
        
        return dfs(0,0)