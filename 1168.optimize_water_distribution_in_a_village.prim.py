from heapq import heappop, heappush


class Solution:
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        # Build ajacency list
        adj = [[] for _ in range(n)]
        for i,j,c in pipes:
            i -= 1
            j -= 1
            adj[i].append((j, c))
            adj[j].append((i, c))
        # Create virtual node
        adj.append([])
        for i,w in enumerate(wells):
            adj[i].append((n, w))
            adj[n].append((i, w))
        # Prim's algorithm
        heap = [(0, n)]
        res = 0
        visited = set()
        while heap:
            w,v = heappop(heap)
            if v in visited:
                continue
            visited.add(v)
            res += w
            for u,w in adj[v]:
                if u in visited:
                    continue
                heappush(heap, (w,u))
        assert(len(visited) == n + 1)
        return res
