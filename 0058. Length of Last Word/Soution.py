class Solution:
    def lengthOfLastWord(self, s):
        """
        type s: str
        rtype: int
        """
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and res > 0:
                return res
            if s[i] != ' ':
                res += 1
        return res