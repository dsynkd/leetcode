class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        self.res = 0

        def sub(s: str, t: str, score: int) -> str:
            stack = []
            for c in s:
                if c == t[1] and stack and stack[-1] == t[0]:
                    stack.pop()
                    self.res += score
                else:
                    stack.append(c)
            return ''.join(stack)

        t = 'ba' if y > x else 'ab'
        score = y if y > x else x

        s = sub(s, t, score)
        sub(s, t[::-1], y if score == x else x)
        return self.res