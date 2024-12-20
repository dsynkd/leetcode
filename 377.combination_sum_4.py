class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        memo = dict()

        def _combinationSum(candidates, target):

            if target == 0:
                return 1
            if target < 0 or len(candidates) == 0:
                return 0
            if target in memo:
                return memo[target]

            num = 0
            for j in range(len(candidates)):
                candidate = candidates[j]
                remainder = target - candidate
                num += _combinationSum(candidates, remainder)

            memo[target] = num
            return num

        return _combinationSum(nums, target)