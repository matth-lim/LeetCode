#include <vector>

using std::vector;

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int res = 0;
        for (auto i: accounts)
        {
            int count = 0;
            for (auto j: i)
            {
                count += j;
            }
            res = max(res, count);
        }
        return res;
    }
};