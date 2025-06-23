class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height)-1
        res = 0
        while i < j:
            area = min(height[i], height[j]) * (j-i)
            res = max(res, area)
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return res