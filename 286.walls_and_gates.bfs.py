from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        m = len(rooms)
        n = len(rooms[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j,0))
        
        visited = set()
        while queue:
            i,j,d = queue.popleft()
            if not (0 <= i < m and 0 <= j < n):
                continue
            if (i,j) in visited or rooms[i][j] == -1:
                continue
            visited.add((i,j))
            if rooms[i][j] != 0:
                rooms[i][j] = d
            queue.append((i + 1, j, d + 1))
            queue.append((i - 1, j, d + 1))
            queue.append((i, j + 1, d + 1))
            queue.append((i, j - 1, d + 1))