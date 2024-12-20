# Time Complexity: O(n)
# Space Complexity: O(1)
# Verdict: Pass

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)