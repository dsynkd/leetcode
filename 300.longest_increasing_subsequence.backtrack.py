# Approach: Backtracking
# Time Complexity: O(2^n)
# Verdict: TLE

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        sequence = []
        self.m = 0
        def dfs(i: int):
            if i == len(nums):
                self.m = max(self.m, len(sequence))
                return
            if not sequence or nums[i] > sequence[-1]:
                sequence.append(nums[i])
                dfs(i+1)
                sequence.pop()
                dfs(i+1)
            else:
                dfs(i+1)
        
        dfs(0)
        return self.m