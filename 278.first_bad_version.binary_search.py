# Approach: Binary Search
# `isBadVersion` is abstracted away
# Verdict: Pass

class Solution:
    def firstBadVersion(self, n):
        l = 0
        r = n-1
        while(r >= l):
            m = l+(r-l)//2
            if isBadVersion(m):
                r = m-1
            else:
                l = m+1
        return l
