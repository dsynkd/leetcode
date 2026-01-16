class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        diff = [0] * (length+1)
        for i,j,c in updates:
            diff[i] += c
            diff[j+1] -= c
        
        res = diff[:-1]
        for i in range(1, len(res)):
            res[i] += res[i-1]
        return res