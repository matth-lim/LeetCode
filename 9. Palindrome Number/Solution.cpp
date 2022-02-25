class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0))
        {
            return false;
        }
        int reverse = 0;
        while (x > reverse)
        {
            int digit = x % 10;
            x = x / 10;
            reverse = reverse * 10 + digit;
        }
        return x == reverse || x == reverse / 10;
    }
};