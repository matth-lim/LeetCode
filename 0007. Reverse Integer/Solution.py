import math

class Solution:
    def reverse(self, x):
        """
        type x: int
        rtype: int
        """
        result = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if result > 214748364 or (result == 214748364 and digit > 7):
                return 0
            if result < -214748364 or (result == -214748364 and digit < -8):
                return 0
            result = result * 10 + digit
        return result