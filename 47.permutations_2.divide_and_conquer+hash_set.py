# Approach: Divide and Conquer, similar to Permutations 1 but using a set and tuples to avoid duplicate
# Unlike the subsets problem, we do not need to sort the tuples, so time complexity remains the same
# Verdict: Pass

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        output = set()

        def _permute(head, tail):
            if len(head) == len(nums):
                output.add(tuple(head))
                return
            for i in range(len(tail)):
                _permute(head + [tail[i]], tail[:i] + tail[i+1:])

        _permute([], nums)
        return [list(a) for a in output]