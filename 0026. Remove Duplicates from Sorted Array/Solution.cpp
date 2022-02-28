#include <vector>

using std::vector;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = 0;
        for (int i = l + 1; i < nums.size(); i++)
        {
            if (nums[l] != nums[i])
            {
                l++;
                nums[l] = nums[i];
            }
        }
        return l + 1;
    }
};