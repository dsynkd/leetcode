class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        S = len(score)
        title = dict()
        scoreSorted = sorted(score)[::-1]
        title[scoreSorted[0]] = "Gold Medal"
        if S > 1:
            title[scoreSorted[1]] = "Silver Medal"
        if S > 2:
            title[scoreSorted[2]] = "Bronze Medal"
        for i in range(3, S):
            title[scoreSorted[i]] = f'{i+1}'
        output = []
        for s in score:
            output.append(title[s])
        return output