class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c = 0
        letterSet = set(brokenLetters)
        for word in text.split(' '):
            isValid = True
            for char in word:
                if char in letterSet:
                    isValid = False
                    break
            if isValid:
                c += 1
        return c