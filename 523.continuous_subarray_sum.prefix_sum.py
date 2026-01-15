class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainders = dict()
        remainders[0] = -1
        Z = 0
        
        for i,n in enumerate(nums):
            Z += n
            r = Z % k
            if r in remainders:
                if i - remainders[r] >= 2:
                    return True
            else:
                remainders[r] = i
            
        return False