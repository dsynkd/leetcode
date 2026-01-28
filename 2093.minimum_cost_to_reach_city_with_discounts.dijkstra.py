from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def minimumCost(self, n: int, highways: list[list[int]], discounts: int) -> int:
        adj = defaultdict(list)
        for i,j,w in highways:
            adj[i].append((j,w))
            adj[j].append((i,w))
        
        heap = [(0,0,discounts)]
        cache = defaultdict(lambda: float('inf'))
        while heap:
            t,v,d = heappop(heap)
            
            if v == n - 1:
                return t
            if t > cache[(v,d)]:
                continue
            
            for u,w in adj[v]:
                T = t + w
                if T < cache[(u, d)]:
                    heappush(heap, (T, u, d))
                    cache[(u, d)] = T
                if d > 0:
                    T = t + w//2
                    if T < cache[(u, d-1)]:
                        heappush(heap, (T, u, d-1))
                        cache[(u, d-1)] = T
        
        return -1