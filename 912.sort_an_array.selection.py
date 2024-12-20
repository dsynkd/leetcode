# Approach: Selection Sort
# Time Complexity: O(n^2)
# Verdict: TLE

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            # Find the minimum
            m = nums[i]
            mi = i
            for j in range(i+1, len(nums)):
                if nums[j] < m:
                    m = nums[j]
                    mi = j
            # Swap the first element with the minimum
            nums[i],nums[mi] = nums[mi],nums[i]
        return nums