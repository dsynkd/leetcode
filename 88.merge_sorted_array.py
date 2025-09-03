class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        j = i = 0
        tmp = nums1.copy()
        for x in range(m+n):
            if not j < len(nums2) or i < m and tmp[i] < nums2[j]:
                nums1[x] = tmp[i]
                i += 1
            else:
                nums1[x] = nums2[j]
                j += 1