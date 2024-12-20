# Approach: Using length of each string and a special character
# Time Complexity: Linear 
# Verdict: Pass

class Solution:

    def encode(self, strs: list[str]) -> str:
        output = ""
        for s in strs:
            output += f'{len(s)}!{s}'
        return output

    def decode(self, s: str) -> list[str]:
        i = 0
        output = []
        while i < len(s):
            strLen = ""
            while s[i] != "!":
                strLen += s[i]
                i += 1
            strLen = int(strLen)
            i += 1
            j = i + strLen
            output.append(s[i:j])
            i = j
        return output