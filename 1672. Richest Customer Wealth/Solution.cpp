#include <vector>
#include <algorithm>

using std::vector, std::max;

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