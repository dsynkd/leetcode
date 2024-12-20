# Approach: "Backtracking" where we pop an item from `nums` each time,
# then append it back into each available position of each permutation (recursive call) of
# the remaining list.

# Techncially not sure if this can be considered backtracking since each base case is a valid solution
# But NeetCode and LeetCode both have Backtracking as a label on this problem

# Verdict: Pass

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        if not nums:
            return [[]]

        perms = []
        item = nums.pop()
        tail_perms = self.permute(nums)
        for p in tail_perms:
            for i in range(len(p)+1):
                # +1 because we are looping over each 'insertion point' in the array and not each item
                # we can also construct newPerm = p[:i] + item + p[i:]
                newPerm = p.copy()
                newPerm.insert(i, item)
                perms.append(newPerm)
        
        return perms