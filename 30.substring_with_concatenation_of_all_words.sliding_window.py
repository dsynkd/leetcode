from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        L = len(words[0])
        permL = L * len(words)
        counter1 = Counter(words)
        output = []

        i = 0
        while i <= len(s) - permL:
            j = i
            counter2 = defaultdict(int)
            c = 0
            while j < i + permL:
                word = s[j:j+L]
                if word in counter1 and counter2[word] < counter1[word]:
                    counter2[word] += 1
                else:
                    break
                j += L
            if j == i + permL:
                output.append(i)
            i += 1
        
        return output