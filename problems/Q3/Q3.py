class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        # charmap stores the current index of a character
        charmap = {}

        ans = int(n > 0) # if len is larger than 0, the output should be at least 1
        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            i = max(charmap.get(s[j], -1), i) # search for nearest repeated char
            ans = max(ans, j - i + 1)   # calculate current length
            charmap[s[j]] = j + 1
        return ans

print(Solution().lengthOfLongestSubstring("au"))