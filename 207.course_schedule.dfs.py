from collections import defaultdict

class Solution:
    def canFinish(self, n: int, prerequisites: list[list[int]]) -> bool:
        adj = defaultdict(list)
        for c,p in prerequisites:
            adj[c].append(p)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            for course in adj[i]:
                if not dfs(course):
                    return False
            visited.remove(i)
            del adj[i]
            return True
        
        for c in range(n):
            visited = set()
            if not dfs(c):
                return False
        
        return True