from heapq import heappop, heappush

class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a,b,c in connections:
            adj[a-1].append((b-1, c))
            adj[b-1].append((a-1, c))
        
        print(adj)
        visited = set()
        heap = [(0, 0)]
        res = 0

        while heap:
            w,v = heappop(heap)
            
            if v in visited:
                continue
            visited.add(v)
            res += w
            
            for u,c in adj[v]:
                if u not in visited:
                    heappush(heap, (c,u))
        
        return res if len(visited) == n else -1