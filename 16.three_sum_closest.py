class Solution:

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        least_diff = None
        res = 0
        for i in range(len(nums)-2):
            r = len(nums) - 1
            l = i+1
            while l != r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(target - s)
                if s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1
                if least_diff is None or diff < least_diff:
                    least_diff = diff
                    res = s
        return res