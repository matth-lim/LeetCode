#include <unordered_map>

using std::unordered_map;

class Solution {
public:
    bool isHappy(int n) {
        unordered_map<int, int> mpp;
        int sum = 0;
        while (sum != 1)
        {
            sum = 0;
            while (n)
            {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }
            if (mpp.find(sum) != mpp.end())
                return false;
            mpp[sum] = sum;
            n = sum;
        }
        return true;
    }
};