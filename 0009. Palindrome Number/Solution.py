class Solution:
    def isPalindrome(self, x):
        """
        type x: int
        rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0): return False
        reverse = 0
        while (x > reverse):
            digit = x % 10
            x = int(x // 10)
            reverse = reverse * 10 + digit
        if x == int(reverse // 10) or x == reverse:
            return True