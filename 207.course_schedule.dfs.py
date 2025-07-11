from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Convert `prerequisites` from an list of pairs into a map of course number to list of requisites
        preReqs = defaultdict(list)
        for i,j in prerequisites:
            preReqs[i].append(j)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if not preReqs[i]:
                return True
            visited.add(i)
            for j in preReqs[i]:
                if not dfs(j):
                    return False
            # Backtrack
            visited.remove(i)
            # We will not need to check prereqs for this course again in the future
            del preReqs[i]
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
