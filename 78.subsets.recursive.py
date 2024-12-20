# Approach: Recursive where we use an increment an index at each call site and make two calls, one that includes an element
# at the index in the new combination and one that does not.
# the base case is where index reaches the end of the nums array, at which point we would have an eligible subset
# Time Complexity: Exponential O(2^n)
# Verdict: Pass

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output = []

        # i = current index in nums
        # combo = current candidate for a subset
        def _subsets(i, combo):
            if i == len(nums):
                output.append(combo)
                return
            
            _subsets(i+1, combo)
            _subsets(i+1, combo + [nums[i]])
        
        _subsets(0, [])
        return output