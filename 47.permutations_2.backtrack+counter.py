# Approach: Same as "46. Permutations" using Backtracking solution, but also adding a Counter
# and not going into a recursive call if the popped element has already been used
# Verdict: Pass

from collections import Counter


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        output = []

        def _permute(perm: list[int], counter: dict[int, int]):
            if len(perm) == len(nums):
                output.append(perm)
                return

            for c in counter:
                if not counter[c]:
                    continue
                newCounter = counter.copy()
                newCounter[c] -= 1
                perms = _permute(perm + [c], newCounter)

        _permute([], Counter(nums))
        return output