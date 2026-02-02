class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        res = 0
        prefixSum = [0] + arr.copy()
        for i in range(1, len(prefixSum)):
            prefixSum[i] += prefixSum[i - 1]
        
        for i in range(len(arr)):
            res += arr[i]
            
            j = (i+1) - 2
            while j > 0:
                res += prefixSum[i+1] - prefixSum[j-1]
                j -= 2
        
        return res