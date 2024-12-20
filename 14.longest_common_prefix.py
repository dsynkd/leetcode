class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ''
        p = ''
        for i in range(0, 200):
            if i >= len(strs[0]):
                return prefix
            p = strs[0][i]
            for s in strs:
                if i >= len(s):
                    return prefix
                if p != s[i]:
                    return prefix
            prefix += p
        return prefix