class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return searchaux(nums, target, 0, len(nums))
    
def searchaux(nums, target, lb, ub) -> int:
    mid = (ub-lb)//2
    index = lb+mid
    if(nums[index] == target):
        return index
    if(mid == 0):
        return -1
    if(nums[index] > target):
        return searchaux(nums, target, lb, index)
    else:
        return searchaux(nums, target, index, ub)
