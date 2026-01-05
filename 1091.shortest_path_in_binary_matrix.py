from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        
        INF = 1e4
        n = len(grid)
        assert(len(grid[0]) == n)

        visited = set()
        q = deque()
        q.append((0,0,1))
        c = 1

        while q:
            (i,j,c) = q.popleft()
            if (i,j) == (n-1,n-1) and grid[i][j] == 0:
                return c
            
            if (not 0 <= i < n) or (not 0 <= j < n) or (i,j) in visited or grid[i][j] == 1:
                continue
            visited.add((i,j))
            q.append((i+1,j+1,c+1))
            q.append((i+1,j,c+1))
            q.append((i,j+1,c+1))
            q.append((i+1,j-1,c+1))
            q.append((i-1,j+1,c+1))
            q.append((i-1,j,c+1))
            q.append((i,j-1,c+1))
            q.append((i-1,j-1,c+1))
        
        return -1