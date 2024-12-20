# HashMap: Similar to "217. Contains Duplicate", we will use a hash data structure,
# but instead of a set, we will use a map, mapping numbers to indices
# We will similary look for duplicates (constant time thanks to HashMap), and subtract
# indices to see if the distance is at most k

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            if num in numMap and i-numMap[num] <= k:
                return True
            numMap[num] = i 
        return False