class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        res = 0

        for num in numset:
            # Only start counting the sequence if a root element is found
            if num-1 in numset:
                continue
            # Count subsequence
            c = 1
            while num+1 in numset:
                c += 1
                num += 1
            res = max(res, c)
        return res