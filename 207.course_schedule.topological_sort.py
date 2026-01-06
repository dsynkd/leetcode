from collections import defaultdict, deque

class Solution:
    def canFinish(self, n: int, prerequisites: list[list[int]]) -> bool:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for c,p in prerequisites:
            adj[c].append(p)
            indegree[p] += 1
        
        Q = deque()
        for i in range(n):
            if not indegree[i]:
                Q.append(i)
        
        c = 0
        while Q:
            node = Q.popleft()
            c += 1
            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    Q.append(v)
                
        return c == n