class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        count = 0

        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            
            if (i,j) in visited:
                return
            
            if grid[i][j] == "0":
                return
            
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(m):
            for j in range(n):
                if (i,j) in visited:
                    continue
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        
        return count