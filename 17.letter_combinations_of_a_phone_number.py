class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digits_map = {
            '2': [
                'a',
                'b',
                'c'
            ],
            '3': [
                'd',
                'e',
                'f'
            ],
            '4': [
                'g',
                'h',
                'i'
            ],
            '5': [
                'j',
                'k',
                'l'
            ],
            '6': [
                'm',
                'n',
                'o'
            ],
            '7': [
                'p',
                'q',
                'r',
                's'
            ],
            '8': [
                't',
                'u',
                'v'
            ],
            '9': [
                'w',
                'x',
                'y',
                'z'
            ]
        }
        l = len(digits)
        combinations = []
        for d in digits:
            letters = digits_map[d]
            if combinations == []:
                combinations = letters
            else:
                new_combinations = []
                for c in combinations:
                    for l in letters:
                        new_combinations.append(c + l)
                combinations = new_combinations
        return combinations