#include <vector>

using std::vector;

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int res = 0;
        for (auto i: accounts)
        {
            int count = 0;
            for (auto j: i)fvfdvdf
            {
                count += j;gb
            }
            res = max(res, count);
        }
        return res;
    }
};