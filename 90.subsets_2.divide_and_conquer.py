# Approach: Similar to Divide and Conquer approach for Subsets 1 except at each recursive call we check the previous
# item in `tail` and do not recurse if it is the same as current item
# !! This approach only works if the given array is sorted, which is the case here but technically not in the problem description !!
# Time Complexity: Exponential O(t^n) where t is the length of 'tail' at each stage
# Verdict: Pass

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        output = []

        def _subsetsWithDup(head, tail):
            output.append(head)
            for i in range(len(tail)):
                # skip over consecutive duplicates in the tail
                if i > 0 and tail[i] == tail[i-1]:
                    continue
                _subsetsWithDup(head + [tail[i]], tail[i+1:])
        
        _subsetsWithDup([], nums)
        return output