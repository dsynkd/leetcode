class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefix = [0] * (n+1)
        suffix = [0] * (n+1)
        
        c = 0
        for i in range(n):
            if s[i] == '0':
                c += 1
            prefix[i+1] = c
        c = 0
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                c += 1
            suffix[i] = c
        
        res = 0
        for i in range(1,n):
            res = max(res, prefix[i] + suffix[i])
        
        return res