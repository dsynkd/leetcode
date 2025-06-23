class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i,j = 0, len(numbers)-1
        while (sum := numbers[i] + numbers[j]) != target:
            assert(i < j) # problem states each test case must have one solution
            if sum > target:
                j -= 1
            else:
                i += 1
        return [i+1,j+1] # +1 because problem asks for 1-based index