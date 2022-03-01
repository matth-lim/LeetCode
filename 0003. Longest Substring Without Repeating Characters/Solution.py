class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l, r = 0, 0
        res = 0
        while (r < len(s)):
            if s[r] in map:
                l = max(map[s[r]] + 1, l)
            map[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res
