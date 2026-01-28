from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for i,j,w in flights:
            adj[i].append((j, w))
        
        heap = [(0, src, 0)]
        cache = [float('inf')] * n
        
        while heap:
            t, v, c = heappop(heap)
            
            if v == dst:
                return t
            if c > k:
                continue
            
            c += 1
            for u,w in adj[v]:
                if c < cache[u]:
                    cache[u] = c
                    heappush(heap, (t + w, v, c))
        
        return -1