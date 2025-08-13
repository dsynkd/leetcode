from collections import defaultdict

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = defaultdict(int)

        def dfs(i,j):
            if not (0 <= i < m) or not (0 <= j < n):
                return 0
            if i == m-1 and j == n-1:
                return 1
            if cache[(i,j)]:
                return cache[(i,j)]
            cache[(i,j)] = dfs(i+1,j) + dfs(i,j+1)
            return cache[(i,j)]

        return dfs(0,0)
