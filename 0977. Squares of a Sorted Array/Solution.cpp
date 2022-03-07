#include <vector>

using std::vector;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res(nums.size(), 0);
        int l = 0, r = nums.size() - 1;
        int i = nums.size() - 1;
        while (l <= r)
        {
            if (abs(nums[l]) < nums[r])
            {
                res[i] = nums[r] * nums[r];
                r--;
            }
            else
            {
                res[i] = nums[l] * nums[l];
                l++;
            }
            i--;
        }
        return res;
    }
};