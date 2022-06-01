import sys
sys.path.append('../helpers/linkedlist')
from ListNode import *

class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1:      'I',
            4:      'IV',
            5:      'V',
            9:      'IX',
            10:     'X',
            40:     'XL',
            50:     'L',
            90:     'XC',
            100:    'C',
            400:    'CD',
            500:    'D',
            900:    'CM',
            1000:   'M'
        }

        res = ''
        keys = list(symbols.keys())
        keys.reverse()
        for di in keys:
            if num == 0:
                return res
            if num >= di:
                repeats = num // di
                res += symbols[di] * repeats
                num = num % di
        return res

if __name__ == '__main__':
    num = 3
    print(Solution().intToRoman(num))
    num = 58
    print(Solution().intToRoman(num))
    num = 1994
    print(Solution().intToRoman(num))