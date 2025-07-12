from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = defaultdict(list)
        for i,j in prerequisites:
            adj[i].append(j)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return False

            if not adj[node]:
                return True

            visited.add(node)
            for n in adj[node]:
                if not dfs(n):
                    return False

            visited.remove(node)
            del adj[node]
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True