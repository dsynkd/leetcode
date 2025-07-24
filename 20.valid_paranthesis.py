class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        m = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in range(1, len(s)):
            c = s[i]
            if c in m:
                if not stack or stack.pop() != m[c]:
                    return False
            else:
                stack.append(c)
        return not stack