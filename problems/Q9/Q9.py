class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    print(Solution().isPalindrome(121))