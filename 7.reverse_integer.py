import math

class Solution:
    def reverse(self, x: int) -> int:
        sign = ''
        if x < 0:
            sign = '-'
            s = str(-x)
        else:
            s = str(x)
        r = ''.join(reversed(s))
        y = int(sign + r)
        bound = math.pow(2, 31)
        if y > bound-1 or y < -bound:
            return 0
        return y
