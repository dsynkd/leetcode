# Tricks to get and set bits obtained here: https://nicolwk.medium.com/bitwise-operations-cheat-sheet-743e09aec5b5

class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i in range(32):
            bit = (n >> i) & 1 # Get bit at `i`th position
            reverse = reverse | (bit << (31-i)) # Set bit at `i-31`th position to the bi8t we just got
        return reverse