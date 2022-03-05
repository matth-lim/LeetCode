class Solution {
public:
    int subtractProductAndSum(int n) {
        int sum1 = 0;
        int sum2 = 1;
        while (n)
        {
            int digit = n % 10;
            sum1 += digit;
            sum2 *= digit;
            n /= 10;
        }
        return sum2 - sum1;
    }
};