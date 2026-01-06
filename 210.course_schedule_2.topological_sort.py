from collections import defaultdict, deque

class Solution:
    def findOrder(self, n: int, prerequisites: list[list[int]]) -> list[int]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for c,p in prerequisites:
            adj[c].append(p)
            indegree[p] += 1
        
        Q = deque()
        for i in range(n):
            if not indegree[i]:
                Q.append(i)
        
        res = []
        while Q:
            node = Q.popleft()
            res.append(node)
            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    Q.append(v)
                
        return res[::-1] if len(res) == n else []