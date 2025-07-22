class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        maxN,minN = 0,100001
        maxI,minI = 0,0
        for i in range(len(nums)):
            n = nums[i]
            if n >= maxN:
                maxN, maxI = n, i
            if n < minN:
                minN, minI = n, i
        res = (len(nums) - maxI - 1) + minI
        if minI > maxI:
            res -= 1
        return res