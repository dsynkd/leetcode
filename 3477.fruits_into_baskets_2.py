class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        taken = [0] * len(baskets)
        for f in fruits:
            for i,b in enumerate(baskets):
                if taken[i]:
                    continue
                if b >= f:
                    taken[i] = True
                    break
        return taken.count(0)