class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        res = 0
        visited = dict()
        while j < len(s):
            c = s[j]
            if c in visited:
                index = visited[c]
                while i <= index:
                    del visited[s[i]]
                    i += 1
            else:
                res = max(res, j-i+1)
            visited[s[j]] = j
            j += 1
        return res