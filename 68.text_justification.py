class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        i = j = 0
        c = 0
        res = []
        while j < len(words):
            if (c := c + len(words[j])) > maxWidth:
                numSpaces = j-i-1
                if numSpaces > 0:
                    sumOfWordLengths = sum([len(w) for w in words[i:j]])
                    spacePerGap = (maxWidth - sumOfWordLengths) // numSpaces
                    spaces = [spacePerGap] * numSpaces

                    # Edge case where it does not divide evenly
                    if (rem := maxWidth - (spacePerGap * numSpaces + sumOfWordLengths)) > 0:
                        for x in range(rem):
                            spaces[x] += 1
                    line = ''
                    for x in range(i,j):
                        line += words[x]
                        if x != j-1:
                            line += ' ' * spaces[x-i]
                    res.append(line)
                else:
                    res.append(words[i] + ' ' * (maxWidth - len(words[i])))
                i = j
                c = len(words[j])
            c += 1
            j += 1
        
        # Last line of text: left-justified
        line = ' '.join(words[i:j])
        line += ' ' * (maxWidth - len(line))
        res.append(line)

        return res