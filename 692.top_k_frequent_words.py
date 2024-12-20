from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        countMap = defaultdict(list)
        for c,v in count.items():
            countMap[v].append(c)
        i = len(words)-1
        output = []
        while i >= 0 and k > 0:
            if i in countMap:
                curWords = sorted(countMap[i])
                L = min(k, len(curWords))
                output += curWords[:L]
                k -= L
            i -= 1
        return output