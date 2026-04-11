class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def can(cap):
            i = 0
            c = 0
            
            while i < len(nums) and c < k:
                if nums[i] <= cap:
                    c += 1
                    i += 2
                else:
                    i += 1
                
            return c >= k

        l, r = min(nums), max(nums)
        
        while l <= r:
            m = l + (r - l) // 2
            if can(m):
                r = m - 1
            else:
                l = m + 1
        
        return l
