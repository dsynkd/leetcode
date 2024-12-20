# Approach: Insertion Sort
# Time Complexity: O(n^2)
# Verdict: TLE

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            j = i
            while j > 0:
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
        return nums