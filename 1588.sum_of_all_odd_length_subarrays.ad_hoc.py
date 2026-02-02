class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        res = 0
        
        for i, a in enumerate(arr):
            left, right = i, n - i - 1
            odd_left = left // 2 + 1
            odd_right = right // 2 + 1
            even_left = (i + 1) // 2
            even_right = (n - i) // 2
            res += a * (odd_left * odd_right + even_left * even_right)
        return res