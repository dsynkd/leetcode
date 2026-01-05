from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for source,dest,cost in flights:
            adj[source].append((dest, cost))
        
        D = defaultdict(lambda: 1e5)
        D[(src,0)] = 0
        heap = [(0, src, 0)]
        
        while heap:
            d, u, c = heappop(heap)
            
            if u == dst:
                return d
            
            if d > D[(u,c)] or c > k:
                continue
            
            c += 1
            for v,w in adj[u]:
                nd = d + w
                if nd >= D[(v,c)]:
                    continue
                D[(v, c)] = nd
                heappush(heap, (nd, v, c))
        
        return -1