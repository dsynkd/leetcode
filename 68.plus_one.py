class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = ''
        for d in digits:
            n += str(d)
        return [int(d) for d in str(int(n)+1)]