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
            distance, v, stops = heappop(heap)
            
            if v == dst:
                return distance
            if stops > k:
                continue
            
            stops += 1
            for u,w in adj[v]:
                if stops < cache[u]:
                    cache[u] = stops
                    heappush(heap, (distance + w, v, stops))
        
        return -1