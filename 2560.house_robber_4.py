class Solution:
    def minCapability(self, nums, k):
        l, r = 1, max(nums)
        N = len(nums)

        while l < r:
            m = (l + r) // 2
            c = 0

            i = 0
            while i < N:
                if nums[i] <= m:
                    c += 1
                    i += 2
                else:
                    i += 1

            if c >= k:
                r = m
            else:
                l = m + 1

        return l