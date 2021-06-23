class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0: return 0
        sign = 1
        num = 0
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        
        for c in str:
            if '0' <= c <= '9':
                num = num * 10 + ord(c) - 48
            
            else:
                break
                
        num *= sign
        
        if -2**31 <= num <= 2**31 - 1:
            return num
        elif -2 ** 31 > num:
            return -2 ** 31
        else:
            return 2 ** 31 - 1


if __name__ == '__main__':
    print(Solution().myAtoi('123'))