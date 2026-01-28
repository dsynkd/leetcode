from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for i,j,w in flights:
            adj[i].append((j, w))
        
        queue = deque()
        queue.append((0, src, 0))
        cache = [float('inf')] * n
        
        while queue:
            w1, v, c = queue.popleft()
            
            if c > k:
                continue
            
            for u,w2 in adj[v]:
                if w1 + w2 < cache[u]:
                    cache[u] = w1 + w2
                    queue.append((w1 + w2, u, c + 1))
        
        return -1 if cache[dst] == float('inf') else int(cache[dst])