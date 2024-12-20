# Approach: Backtracking + HashSet + Sort
# Time Complexity: Exponential O(2^n.n.log(n)); 2^n is the number of recursive calls; n.log(n) for sort
# Verdict: Pass

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        output = set()

        def backtrack(i, combo):
            if i == len(nums):
                output.add(tuple(sorted(combo)))
                return
            backtrack(i+1, combo)
            backtrack(i+1, combo + [nums[i]])
        
        backtrack(0, [])
        return [list(a) for a in output]