# Approach: Sliding Window
# also using a "have" counter to meet eligible criteria instead of comparing hash tables
# Verdict: pass

from collections import Counter, defaultdict
from copy import deepcopy

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = Counter(t)
        scount = defaultdict(int)
        res = ""
        have, need = 0, len(t)
        i,j = 0,0
        while j < len(s):
            c = s[j]
            scount[c] += 1
            if scount[c] <= tcount[c]:
                have += 1

            while have == need:
                if not res or len(s[i:j+1]) < len(res):
                    res = s[i:j+1]
                c = s[i]
                scount[c] -= 1
                if c in tcount and scount[c] < tcount[c]:
                    have -= 1
                i += 1
            j += 1
        return res