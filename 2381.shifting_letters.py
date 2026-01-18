class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for i,j,d in shifts:
            c = 1 if d else -1
            diff[i] += c
            diff[j+1] -= c
        
        diff = diff[:-1]
        for i in range(1, n):
            diff[i] += diff[i-1]
        
        res = ''
        R = ord('z') - ord('a') + 1

        for i in range(n):
            shift = diff[i] if diff[i] > 0 else diff[i] + R
            c = (ord(s[i]) - ord('a') + shift) % R + ord('a')
            res += chr(c)
        
        return res