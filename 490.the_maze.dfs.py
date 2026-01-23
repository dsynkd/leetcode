class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        D = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def dfs(x,y):
            assert((0 <= x < m) and (0 <= y < n) and maze[x][y] == 0)
            
            if (x,y) == tuple(destination):
                return True
            
            if (x,y) in visited:
                return False
            visited.add((x,y))
            
            for dx,dy in D:
                i,j = x,y
                while (0 <= i+dx < m) and (0 <= j+dy < n) and maze[i+dx][j+dy] == 0:
                    i += dx
                    j += dy
                if dfs(i,j):
                    return True
            
            return False
        
        i,j = start
        return dfs(i, j)