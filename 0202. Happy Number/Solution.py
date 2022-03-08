class Solution:
    def isHappy(self, n):
        """
        type n: int
        rtype: bool
        """
        maps = {}
        sums = 0
        while (sums != 1):
            sums = 0
            while n:
                digit = n % 10
                sums += digit ** 2
                n = n // 10
            if sums in maps:
                return False
            maps[sums] = sums
            n = sums
        return True