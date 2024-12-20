# 1. This is a cycle detection problem
# 2. The given edges do not always necessarily flow from the smaller index to the bigger index, so we need to construct the adjancy list both ways
# 3. Since edges flow both ways, in order to not traverse back to the node we came from and count that as a 'cycle' we need to pass the prev node

from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        visited = set()

        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def hasCycle(node, prev):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if neighbor in visited:
                    return True
                if hasCycle(neighbor, node):
                    return True
            return False
        
        return (not hasCycle(0, -1) and len(visited) == n)
