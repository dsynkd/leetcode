# Time Complexity: O(n)
# Space Complexity: O(1)
# Verdict: Pass

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return sum(range(n+1)) - sum(nums)