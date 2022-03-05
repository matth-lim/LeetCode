class Solution:
    def subtractProductAndSum(self, n):
        """
        type n: int
        rtype: int
        """
        sum1 = 0
        sum2 = 1
        while n:
            digit = n % 10
            sum1 += digit
            sum2 *= digit
            n = n // 10
        return sum2 - sum1