# Approach: Backtracking, similar to recursive version but instead of popping element each time
# and making a recursive call, we just loop through each item in `nums` and continuously update
# out permutations list
# Verdict: Pass

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        perms = [[]]
        for n in nums:
            res = []
            for p in perms:
                for i in range(len(p)+1):
                    res.append(p[:i] + [n] + p[i:])
            perms = res
        
        return perms