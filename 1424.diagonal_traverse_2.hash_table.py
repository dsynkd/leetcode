from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        D = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                D[i+j].append(nums[i][j])
        
        res = []
        for k,v in D.items():
            res += v[::-1]
        return res