class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        L = len(nums)
        i = 0
        while i < L:
            if nums[i] == val:
                del nums[i]
                L -= 1
            else:
                i += 1
        return len(nums)