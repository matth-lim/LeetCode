#include <vector>

using std::vector;

class Solution {
public:
    int removeElement_1(vector<int>& nums, int val) {
        int l = 0, r = nums.size();
        while(l < r)
        {
            if (nums[l] == val)
            {
                nums[l] = nums[r - 1];
                r--;
            }
            else
                l++;
        }
        return r;
    }
};