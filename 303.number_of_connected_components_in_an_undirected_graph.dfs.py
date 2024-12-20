# Similar to "261. Graph Valid Trees", we do a graph traversal and store all visited nodes, then increment a counter for each time we
# need to do this

from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(node, prev):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if neighbor in visited:
                    continue
                dfs(neighbor, node)
        
        count = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i, -1)
            count += 1
        return count