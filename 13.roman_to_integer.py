class Solution:

    def romanToInt(self, s: str) -> int:
        roman_map = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        output = 0
        prev = None
        for i,c in enumerate(s):
            current_val = roman_map[c]
            if prev != None and roman_map[prev] < current_val:
                output -= roman_map[prev]
                output += (current_val - roman_map[prev])
            else:
                output += current_val
            prev = c
        return output