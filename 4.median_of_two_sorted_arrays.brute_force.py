# Approach: Brute Force, append two arrays together and then sort the resulting array, then get the median
# Time Complexity: O(N.log(N)) where N = m+n; Quick sort
# Verdict: Pass, but does not satisfy problem statement

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a = nums1 + nums2
        a.sort()

        if len(a) % 2 == 1:
            return a[len(a) // 2]
        else:
            return (a[len(a) // 2] + a[len(a) // 2 - 1]) / 2