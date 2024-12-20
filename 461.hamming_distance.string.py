class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming = 0
        # Convert to binary forms
        xb = list(bin(x)[2:])
        yb = list(bin(y)[2:])
        while xb and yb:
            d1 = xb.pop()
            d2 = yb.pop()
            if d1 != d2:
                hamming += 1
        # count remaining 1s
        for d in xb or yb:
            if d == '1':
                hamming += 1
        return hamming