# Approach: "Divide and Conquer" where we continously divide the array into a 'head' (intially []) and 'tail' (initially nums) section,
# and continously construct new heads by appending looping over and appending each element from 'tail',
# Once the length of head has reached the length of `nums` we have a permutation
# Verdict: Pass

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        output = []

        def _permute(head, tail):
            if len(head) == len(nums):
                output.append(head)
                return
            
            for i in range(len(tail)):
                newHead = head + [tail[i]]
                newTail = tail[i+1:]
                _permute(newHead, newTail)

        _permute([], nums)
        return output