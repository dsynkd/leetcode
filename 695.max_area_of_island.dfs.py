class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        visited = set()
        
        def dfs(i,j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if (i,j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i,j))
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i, j-1)
        
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        
        return res