from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j,0))

        res = 0
        visited = set()
        while queue:
            (i,j,d) = queue.popleft()
            if not (0 <= i < n) or not (0 <= j < n) or (i,j) in visited:
                continue
            queue.append((i-1, j,   d+1))
            queue.append((i+1, j,   d+1))
            queue.append((i  , j-1, d+1))
            queue.append((i  , j+1, d+1))
            visited.add((i,j))
            res = d
        
        return res or -1