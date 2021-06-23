class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        segSize = (numRows - 1) * 2
        s = list(s)
        endings = [''] * ((len(s) + segSize - 1) // segSize * segSize - len(s))
        s += endings

        res = ''
        for i in range(0, numRows):
            for j in range(0, len(s) // segSize):
                res += s[j * segSize + i]
                if i != 0 and i != numRows - 1:
                    res += s[(j + 1) * segSize - i]
        return res


if __name__ == '__main__':
    print(Solution().convert('PAYPALISHIRING', 4))