from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        Q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    Q.append((i,j,0))

        res = 0
        V = set()
        while Q:
            (i,j,d) = Q.popleft()
            if not (0 <= i < n) or not (0 <= j < n):
                continue
            if (i,j) in V:
                continue
            V.add((i,j))
            res = d
            Q.append((i-1, j,   d+1))
            Q.append((i+1, j,   d+1))
            Q.append((i  , j-1, d+1))
            Q.append((i  , j+1, d+1))
        
        return res or -1