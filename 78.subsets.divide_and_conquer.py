# Approach: Divide and Conquer where we divide the given list into a 'head' by appending the first item from the
# list, and a 'tail' by removing the first item from the list.
# Time Complexity: O()
# Verdict: Pass

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output = []

        def _subsets(head, tail):
            output.append(head)
            for i in range(len(tail)):
                newHead = head + [tail[i]]
                newTail = tail[i+1:]
                _subsets(newHead, newTail)
        
        _subsets([], nums)
        return output