# Approach: Brute Force

class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        b = (32-len(b)) * '0' + b
        return int(''.join(reversed(b)), 2)