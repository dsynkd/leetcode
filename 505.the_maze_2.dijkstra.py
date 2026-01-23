from heapq import heappop, heappush

class Solution:
    def shortestDistance(self, maze: list[list[int]], start: list[int], destination: list[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        D = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        x,y = start
        queue = []
        queue.append((0,x,y)) 
        while queue:
            c,x,y = heappop(queue)
            if (x,y) == tuple(destination):
                return c
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for dx,dy in D:
                i,j = x,y
                d = c
                while ((0 <= i < m) and (0 <= j < n) and maze[i][j] == 0):
                    i += dx
                    j += dy
                    d += 1
                heappush(queue, (d-1, i-dx, j-dy))
        
        return -1