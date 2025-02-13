class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        m = dict()
        def _wordBreak(s: str, wordDict: list[str]):

            if s == '':
                return True
            if s in m:
                return m[s]

            for word in wordDict:
                if not (word in s and s.index(word) == 0):
                    continue
                l = len(word)
                if _wordBreak(s[l:], wordDict):
                    m[s] = True
                    return True

            m[s] = False
            return False
        
        return _wordBreak(s, wordDict)