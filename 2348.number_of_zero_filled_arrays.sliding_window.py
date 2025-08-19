class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        i = j = 0
        res = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
                continue
            res += sum(range(j-i+1))
            j += 1
            i = j
        res += sum(range(j-i+1))
        return res