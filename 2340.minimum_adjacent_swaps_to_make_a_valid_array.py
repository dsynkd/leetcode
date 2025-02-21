class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minV, maxV = min(nums),max(nums)
        count = 0
        for i in range(len(nums)):
            n = nums[i]
            if n == minV:
                count += i
                break
        for j in range(len(nums)-1,-1,-1):
            n = nums[j]
            if n == maxV:
                count += len(nums)-j-1
                break
        if i > j:
            count -= 1
        return count