class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i,j = 0, len(numbers)-1
        while (sum := numbers[i] + numbers[j]) != target:
            assert(i < j)
            if sum > target:
                j -= 1
            else:
                i += 1
        # +1 because it is asked by problem
        return [i+1,j+1]