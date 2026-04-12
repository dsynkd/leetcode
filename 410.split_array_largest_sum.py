class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        N = len(nums)

        def can(X):
            c,s,i = 0,0,0
            while c < k and i < N:
                if s + nums[i] > X:
                    c += 1
                    s = 0
                else:
                    s += nums[i]
                    i += 1
            return i == N
        
        i, j = 0, sum(nums)
        while i <= j:
            m = i + (j-i) // 2
            if can(m):
                j = m-1
            else:
                i = m+1
        return i