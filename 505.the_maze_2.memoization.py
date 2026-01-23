class Solution:
    def shortestDistance(self, maze: list[list[int]], start: list[int], destination: list[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        D = [(1,0), (-1,0), (0,1), (0,-1)]
        cache = dict()
        self.res = float('inf')

        def dfs(x,y,c):
            assert((0 <= x < m) and (0 <= y < n) and maze[x][y] == 0)
            
            if (x,y) == tuple(destination):
                self.res = min(self.res, c)
                return
            
            for dx,dy in D:
                i,j = x,y
                d = c
                while (0 <= i+dx < m) and (0 <= j+dy < n) and maze[i+dx][j+dy] == 0:
                    i += dx
                    j += dy
                    d += 1
                if (i,j) not in cache or cache[(i,j)] > d:
                    cache[(i,j)] = d
                    dfs(i,j,d)
        
        i,j = start
        dfs(i, j, 0)
        return -1 if self.res == float('inf') else self.res