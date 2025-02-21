class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = set()
        def dfs(i):
            if not 0 <= i < len(arr):
                return False
            n = arr[i]
            if n == 0:
                return True
            if i in visited:
                return False
            visited.add(i)
            return dfs(i - n) or dfs(i + n)
        
        return dfs(start)