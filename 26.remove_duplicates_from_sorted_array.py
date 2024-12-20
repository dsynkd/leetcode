class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s = set()
        L = len(nums)
        i = 0
        while i < L:
            if nums[i] in s:
                del nums[i]
                L -= 1
            else:
                s.add(nums[i])
                i += 1
        return len(nums)