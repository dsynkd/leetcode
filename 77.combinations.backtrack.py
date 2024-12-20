# Approach: Backtracking
## Advantage of backtracking over passing 'combo' as an additional parameter recursively
## is that we use less memory by not having to make a copy of it at every call site
# Verdict: Pass

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = list(range(1,n+1))
        output = []

        combo = []
        def dfs(i: int):
            if i == n:
                if len(combo) == k:
                    output.append(combo.copy())
                return
            combo.append(nums[i])
            dfs(i+1)
            # Backtrack
            combo.pop()
            dfs(i+1)
        
        dfs(0)
        return output

print(Solution().combine(4, 2))