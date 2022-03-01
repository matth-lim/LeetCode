class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        for x in range(len(s)):
            l = x
            r = x
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > reslen:
                    res = s[l:r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1
            l = x
            r = x + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > reslen:
                    res = s[l:r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1
        return res