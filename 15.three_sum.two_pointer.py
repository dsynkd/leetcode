class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            # skip over duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j,k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k] + nums[i]
                if sum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j += 1
                    # skip over duplicates
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        return res