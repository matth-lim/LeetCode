#include <vector>
#include <algorithm>

using std::vector;

class Solution {
public:
    double average(vector<int>& salary) {
        int sum = 0;
        for (int i:salary)
            sum += i;
        return (sum - *max_element(begin(salary), end(salary)) - *min_element(begin(salary), end(salary))) / ((salary.size() - 2) * 1.0);
    }
};