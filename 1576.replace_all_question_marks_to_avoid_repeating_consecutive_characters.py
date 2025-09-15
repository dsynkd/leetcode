class Solution:
    def modifyString(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            c = s[i]
            if c == '?':
                for a in ['a', 'b', 'c']:
                    if (not res or res[-1] != a) and (i == len(s)-1 or s[i+1] != a):
                        res += a
                        break
            else:
                res += c
        return res