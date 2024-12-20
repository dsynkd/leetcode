class Solution:
    def intToRoman(self, num: int) -> str:
        map = {
            # 1,2,3,...
            1: {
                1: 'I',
                2: 'II',
                3: 'III',
                4: 'IV',
                5: 'V',
                6: 'VI',
                7: 'VII',
                8: 'VIII',
                9: 'IX'
            },
            # 10,11,12,... 90
            2: {
                1: 'X',
                2: 'XX',
                3: 'XXX',
                4: 'XL',
                5: 'L',
                6: 'LX',
                7: 'LXX',
                8: 'LXXX',
                9: 'XC'
            },
            # 100, 200, ..., 900
            3: {
                1: 'C',
                2: 'CC',
                3: 'CCC',
                4: 'CD',
                5: 'D',
                6: 'DC',
                7: 'DCC',
                8: 'DCCC',
                9: 'CM'
            },
            # 1000, 2000, 3000
            4: {
                1: 'M',
                2: 'MM',
                3: 'MMM'
            }
        }
        s = str(num)
        o = ''
        for i in range(len(s)):
            r = len(s) - i
            c = s[i]
            if c == '0': continue
            o += map[r][int(c)]
        return o