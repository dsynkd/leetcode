from collections import defaultdict

class Solution:
    def numTriplets(self, nums1:list[int], nums2: list[int]) -> int:
        res = 0
        for n1 in nums1:
            factors = defaultdict(int)
            for n2 in nums2:
                if (n1*n1)%n2 == 0:
                    factor = (n1*n1)//n2
                    res += factors[factor]
                    factors[n2] += 1
        
        for n1 in nums2:
            factors = defaultdict(int)
            for n2 in nums1:
                if (n1*n1)%n2 == 0:
                    factor = (n1*n1)//n2
                    res += factors[factor]
                    factors[n2] += 1
        return res
        