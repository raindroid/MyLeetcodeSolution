class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = int(str(x)[::-1])
        if res > 2147483647 or res < -2147483648:
            return 0
        return res * sign

if __name__ == '__main__':
    print(Solution().reverse(123))