class Solution:
    def myAtoi(self, s: str) -> int:

        # Skip leading whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
            continue
        if i == len(s):
            return 0

        # Accumulate digits into n
        n = ''
        if s[i] == '-' or s[i] == '+':
            n = s[i]
            i += 1
        while i < len(s) and s[i].isdigit():
            n += s[i]
            i += 1

        if n == '' or n == '-' or n == '+':
            return 0

        # Do the conversion and limit check
        n = int(n)
        if n > 2147483647:
            return 2147483647
        elif n < -2147483648:
            return -2147483648
        else:
            return n