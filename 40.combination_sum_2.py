from enum import unique
from math import comb
from re import A

class Solution:

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        def _combinationSum(candidates, target):

            if target == 0:
                return [[]]
            if target < 0:
                return []

            combination_sums = []

            prev = -1
            for i in range(len(candidates)):
                candidate = candidates[i]

                if candidate == prev: continue
                prev = candidate

                new_candidates = candidates[:i] + candidates[i+1:]
                remainder = target - candidate
                res = _combinationSum(new_candidates, remainder)
                for i in range(len(res)):
                    combination = res[i] + [candidate]
                    combination_sums.append(sorted(combination))

            return combination_sums

        def unique(c: list):
            s = set(tuple(i) for i in c)
            s = list(list(i) for i in s)
            return s

        c = sorted(candidates)
        answer = _combinationSum(c, target)
        return unique(answer, c)