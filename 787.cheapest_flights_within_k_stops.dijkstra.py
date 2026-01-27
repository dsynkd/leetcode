from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for source,dest,cost in flights:
            adj[source].append((dest, cost))
        
        heap = [(0, src, 0)]
        cache = [float('inf')] * n
        
        while heap:
            w1, v, c = heappop(heap)
            
            if v == dst:
                return w1
            if c > k:
                continue
            cache[v] = c
            
            c += 1
            for u,w2 in adj[v]:
                if c + 1 < cache[u]:
                    heappush(heap, (w1 + w2, v, c + 1))
        
        return -1