class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        dif = float('inf')
        res = 0
        for i in range(len(nums)):
            j,k = i+1,len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif s < target:
                    j += 1
                else:
                    k -= 1
                if abs(target - s) < dif:
                    dif = abs(target - s)
                    res = s
        return res