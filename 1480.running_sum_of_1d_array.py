class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        s = 0
        for n in nums:
            s += n
            res.append(s)
        return res