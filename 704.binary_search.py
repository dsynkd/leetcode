class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while i <= j:
            k = i + (j-i)//2
            if nums[k] > target:
                j = k-1
            elif nums[k] < target:
                i = k+1
            else:
                return k
        return -1