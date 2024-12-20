#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = len(nums)
        l, r = 0, L-1
        while l < r:
            m = l + (r-l)//2


# @lc code=end

