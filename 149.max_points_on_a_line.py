class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        res = 1

        for i in range(len(points)):
            x1, y1 = points[i]
            # p/q = r/s
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                assert(not (x1 == x2 and y1 == y2))
                p = (y2 - y1)
                q = (x2 - x1)
                c = 2
                
                for k in range(j+1, len(points)):
                    x3,y3 = points[k]
                    r = (y3 - y1)
                    s = (x3 - x1)
                    if p * s == r * q:
                        c += 1
                
                res = max(res, c)
        
        return res
