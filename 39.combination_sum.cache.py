class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        cache = dict()

        def _combinationSum(candidates, target):

            if target == 0:
                return [[]]
            if target < 0:
                return []
            if target in cache:
                return cache[target]

            combination_sums = []
            for j in range(len(candidates)):
                candidate = candidates[j]
                remainder = target - candidate
                res = _combinationSum(candidates, remainder)
                for i in range(len(res)):
                    c = res[i] + [candidate]
                    combination_sums.append(sorted(c))

            cache[target] = combination_sums
            return combination_sums


        def unique(c: list):
            s = set(tuple(i) for i in c)
            s = list(list(i) for i in s)
            return s

        return unique(_combinationSum(candidates, target))