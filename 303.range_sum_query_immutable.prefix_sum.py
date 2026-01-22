class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefixSum = [0] + nums.copy()
        
        for i in range(1, len(self.prefixSum)):
            self.prefixSum[i] += self.prefixSum[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1] - self.prefixSum[left]
