class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        res = []
        L = len(p)
        ps = Counter(s[:len(p)])
        pc = Counter(p)
        if ps == pc:
            res.append(0)
        
        for i in range(1, len(s) - L + 1):
            j = i + L
            ps[s[i-1]] -= 1
            ps[s[j-1]] += 1
            if ps == pc:
                res.append(i)
        
        return res