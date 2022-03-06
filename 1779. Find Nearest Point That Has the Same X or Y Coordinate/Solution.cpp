#include <vector>

using std::vector;

class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int dis = INT_MAX;
        int res = -1;
        for (int i = 0; i < points.size(); i++)
        {
            if (points[i][0] == x || points[i][1] == y)
            {
                int distance = abs(x - points[i][0]) + abs(y - points[i][1]);
                if (distance < dis)
                {
                    dis = distance;
                    res = i;
                }
            }
        }
        return res;
    }
};