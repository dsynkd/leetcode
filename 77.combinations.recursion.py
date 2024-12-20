# Same as "78. Subsets"

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = list(range(1,n+1))
        output = []

        def dfs(i: int, combo: list[int]):
            if i == n:
                if len(combo) == k:
                    output.append(combo)
                return
            dfs(i+1, combo + [nums[i]])
            dfs(i+1, combo)
        
        dfs(0, [])
        return output