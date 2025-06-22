class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        remainders = dict()
        for i,n in enumerate(nums):
            if n in remainders:
                return [i, remainders[n]]
            else:
                remainders[target - n] = i
        # should not arrive here
        return []
