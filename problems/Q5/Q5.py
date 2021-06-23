class Solution:
    def longestPalindrome(self, s: str) -> str: # expanding sliding window
        if len(s) == 0 or len(s) == 1: return s
        i = 0
        res = s[0]
        while i <= len(s) - len(res) // 2:
            p = 0
            while i - p >= 0 and i + p < len(s) and s[i - p] == s[i + p]:
                p += 1
            p -= 1
            # print('p={},i={},'.format(p,i),'1=', s[i - p: i + p + 1])
            if 2 * p + 1 > len(res):
                res = s[i - p: i + p + 1]
                
            p = 0
            while i - p >= 0 and i + p + 1 < len(s) and s[i - p] == s[i + p + 1]:
                p += 1
            p -= 1
            # print('p={},i={},'.format(p,i),'2=', s[i - p : i + p + 2])
            if 2 * p + 2 > len(res):
                res = s[i - p : i + p + 2]
                
            i += 1
                
        return res


if __name__ == '__main__':
    print(Solution().longestPalindrome('babad'))