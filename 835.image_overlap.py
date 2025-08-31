class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        
        n = len(img1)
        assert(n == len(img1[0]) and n == len(img2) and n == len(img2[0]))

        def shift(a,b):
            c = 0
            for i in range(n):
                for j in range(n):
                    if 0 <= i+a < n and 0 <= j+b < n:
                        c += img1[i+a][j+b] & img2[i][j]
            return c

        self.res = 0
        for i in range(-n,n):
            for j in range(-n,n):
                self.res = max(self.res, shift(i,j))
        return self.res
