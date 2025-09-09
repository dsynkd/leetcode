class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        res = [0] * len(nums)
        for i,n in enumerate(nums):
            res[(i+k)%len(nums)] = n
        for i,n in enumerate(res):
            nums[i] = n