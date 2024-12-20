# Approach: Bubble Sort (Brute Force)
# Time Complexity: O(n^2)
# Verdict: TLE

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums