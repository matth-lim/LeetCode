class Solution:
    def myAtoi(self, s):
        """
        type s: str
        rtype: int
        """
        result = 0
        index = 0
        negative = False
        s = s.strip()
        if s == "":
            return 0
        if s[index] == '-':
            negative = True
            index += 1
        elif s[index] == '+':
            index += 1
        while index < len(s) and ord(s[index]) >= ord('0') and ord(s[index]) <= ord('9'):
            digit = ord(s[index]) - ord('0')
            if (result > 214748364 or (result == 214748364 and digit > 7)):
                if negative:
                    return -2147483648
                else:
                    return 2147483647
            result = result * 10 + digit
            index += 1
        if (negative):
            return -result
        return result