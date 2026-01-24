class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        wordSet = set(words)
        res = []
        for i in range(len(text)):
            for j in range(i, len(text)):
                if text[i:j+1] in wordSet:
                    res.append([i,j])
        return res