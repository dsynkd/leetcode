class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0,1]
        # Create adjacency list
        adj = [[] for _ in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            while leaves:
                u = leaves.pop()
                v = adj[u].pop()
                adj[v].remove(u)
                if len(adj[v]) == 1:
                    new_leaves.append(v)
            leaves = new_leaves

        return leaves