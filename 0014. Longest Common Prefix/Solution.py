class Solution:
    def longestCommonPrefix(self, strs):
        """
        type strs: List[str]
        rtype: str
        """
        res = ""
        for x in range(len(min(strs))):
            for y in range(1, len(strs)):
                if strs[0][x] != strs[y][x]:
                    return res
            res += strs[0][x]
        return res