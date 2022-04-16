class Solution:
    def maximumWealth(self, accounts):
        """
        type accounts: List[List[int]]
        rtype: int
        """
        res = 0
        for x in accounts:
            res = max(res, sum(x))
        return res