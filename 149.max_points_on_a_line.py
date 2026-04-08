class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        res = 1

        for i in range(len(points)):
            x1, y1 = points[i]
            # p/q = r/s
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                assert(not (x1 == x2 and y1 == y2)) # Points are unique
                a = (y2 - y1)
                b = (x2 - x1)
                c = 2
                
                for k in range(j+1, len(points)):
                    x3,y3 = points[k]
                    c = (y3 - y1)
                    d = (x3 - x1)
                    if a * d == c * b:
                        c += 1
                
                res = max(res, c)
        
        return res
