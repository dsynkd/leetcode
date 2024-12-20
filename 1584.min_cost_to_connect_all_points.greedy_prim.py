# "Minimum Spanning Tree"
# Approach: Greedy - Prim's Algorithm
# Time Complexity: n^2.log(n)
# Verdict: Pass

from heapq import heappop, heappush

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        total = 0
        frontier = []
        p1 = points[0]
        visited = set()
        visited.add(tuple(p1))

        while len(visited) < len(points):
            for p2 in points:
                if p1 == p2 and tuple(p2) not in visited:
                    distance = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
                    heappush(frontier, (distance, tuple(p2)))
            distance,p1 = heappop(frontier)
            if p1 not in visited:
                visited.add(p1)
                total += distance
        
        return total