# Same approach as brute force but abstracted away
# Time Complexity: `median` calls `sorted`, so O(N.log(N))
# Verdict: Pass

import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return statistics.median(nums1 + nums2)