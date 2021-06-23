class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(i, j):
            if j <= -1:
                return i == -1
            if i == -1:
                return helper(i, j - 2) if p[j] == '*' else False
            if s[i] == p[j]:
                return helper(i - 1, j - 1)
            if p[j] == '.':
                return helper(i - 1, j - 1)
            if p[j] == '*':
                if p[j - 1] == '.' or p[j - 1] == s[i]:
                    if helper(i - 1, j):
                        return True
                return helper(i, j - 2)
        return helper(len(s) - 1, len(p) - 1)


if __name__ == "__main__":
    print(Solution().isMatch('aaab', 'a*b'))