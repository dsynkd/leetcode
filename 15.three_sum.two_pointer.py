# Similar to 'Memoization' solution, but we sort the array initially to prevent having to sort it for
# each obtained subset
# Time Complexity: O(n^2) 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        memo = dict()

        def twoSum(nums: list[int], target: int):
            output = []
            remainders = dict()
            for n in nums:
                remainder = target - n
                if n in remainders:
                    output.append([n, remainders[n]])
                remainders[remainder] = n
            return output

        # Using set to prevent duplicates
        output = set()

        # For every item in nums, set target = 0-num and run two sum on the remainder of the array
        # Cache the results for each run so we do not have to repeat the same operation for repeated numbers
        for i in range(len(nums)):
            n = nums[i]
            if n in memo:
                continue
            res = twoSum(nums[:i] + nums[i+1:], -n)
            # Add the number back into the combinations
            for j in range(len(res)):
                res[j] += [n]
                # Need to sort to detect duplicates to work
                output.add(tuple(sorted(res[j])))

            memo[n] = True

        return [list(a) for a in output]