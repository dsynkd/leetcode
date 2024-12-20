# Trick: Realizing that, for any N in nums, if N-1
# is not in nums, then that means that N is a root
# of a subsequence.
# Furthermore, this lookup can be done in constant time using a HashSet
# Once we detect subsequence root, we can then continuously look for consequtive numbers (which again can be done in constant time using HashSet), which will give us the subsequence length

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        maxL = 0
        for n in nums:
            if n-1 not in numset:
                # sequence root detected
                i = 0
                while (n+i) in numset:
                    # count length of sequence
                    i += 1
                if i > maxL:
                    maxL = i
        return maxL