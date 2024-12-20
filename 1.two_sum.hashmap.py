# HashMap: Another example of use case

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        remainders = dict()
        for i in range(len(nums)):
            n = nums[i]
            if n in remainders:
                return [i, remainders[n]]
            else:
                remainders[target - n] = i
        # Problem states assumption that all inputs have one solution
        return []
