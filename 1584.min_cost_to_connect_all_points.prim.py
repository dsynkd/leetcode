from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        res = 0
        x,y = points[0]
        heap = [(0, x, y)]
        visited = set()

        while heap:
            c, x1, y1 = heappop(heap)
            if (x1, y1) in visited:
                continue
            visited.add((x1, y1))
            res += c
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                c = abs(x1 - x2) + abs(y1 - y2)
                if (x2, y2) not in visited:
                    heappush(heap, (c, x2, y2))
        
        assert(len(visited) == len(points))
        return res