class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        N = len(nums)

        def can(X):
            i = 0
            c = 0

            while i < N and c <= maxOperations:
                c += (nums[i] - 1) // X
                i += 1

            return i == N and c <= maxOperations
        
        i, j = 1, max(nums)
        while i <= j:
            m = i + (j - i) // 2
            if can(m):
                j = m-1
            else:
                i = m+1
        
        return i