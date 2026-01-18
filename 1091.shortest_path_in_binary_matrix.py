from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        assert(n == len(grid[0]))
        if grid[0][0] == 1:
            return -1
        Q = deque()
        Q.append((0,0,1))
        visited = set()

        while Q:
            (i,j,d) = Q.popleft()
            if (i,j) == (n-1,n-1):
                if grid[i][j] == 1:
                    return -1
                return d
            
            if (not 0 <= i < n) or (not 0 <= j < n):
                continue
            if (i,j) in visited or grid[i][j] == 1:
                continue
            visited.add((i,j))
            d += 1
            Q.append((i+1, j+1, d))
            Q.append((i+1, j,   d))
            Q.append((i,   j+1, d))
            Q.append((i+1, j-1, d))
            Q.append((i-1, j+1, d))
            Q.append((i-1, j,   d))
            Q.append((i,   j-1, d))
            Q.append((i-1, j-1, d))
        
        return -1