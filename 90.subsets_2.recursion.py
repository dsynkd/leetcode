class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        output = []

        def _subsetsWithDup(head, tail):
            output.append(head)
            for i in range(len(tail)):
                # skip over consecutive duplicates in the tail
                if i > 0 and tail[i] == tail[i-1]:
                    continue
                _subsetsWithDup(head + [tail[i]], tail[i+1:])
        
        _subsetsWithDup([], nums)
        return output