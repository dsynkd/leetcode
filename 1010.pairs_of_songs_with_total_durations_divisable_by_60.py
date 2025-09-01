from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        n = len(time)
        rems = defaultdict(int)
        res = 0
        for n in time:
            r = n%60
            if r == 0:
                res += rems[0]
            else:
                res += rems[60-r]
            rems[r] += 1
        return res