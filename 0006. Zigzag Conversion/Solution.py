class Solution:
    def convert(self, s, numRows):
        """
        type s: str
        type numRows: int
        rtype: str
        """
        if numRows == 1: return s
        res = ""
        for x in range(numRows):
            increament = 2 * (numRows - 1)
            for y in range(x, len(s), increament):
                print(y)
                res += s[y]
                if x > 0 and x < numRows - 1 and y + increament - 2 * x < len(s):
                    res += s[y + increament - 2 * x]
        return res