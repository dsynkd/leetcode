class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        maxStreak = -1
        nums = set(nums)
        for n in nums:
            streak = -1
            m = n
            while (m := m*m) in nums:
                if streak == -1:
                    streak = 2
                else:
                    streak += 1
            maxStreak = max(maxStreak, streak)
        return maxStreak