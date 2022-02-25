#include <vector>
#include <unordered_map>

using std::vector, std::unordered_map;

class Solution {
public:
    vector<int> twoSum_1(vector<int>& nums, int target) {
        vector<int> result;
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    result.push_back(i);
                    result.push_back(j);
                }
            }
        }
        return result;
    }
    
    vector<int> twoSum_2(vector<int>& nums, int target) {
        vector<int> result;
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++)
        {
            if (hash.find(target - nums[i]) != hash.end())
            {
                result.push_back(hash[target - nums[i]]);
                result.push_back(i);
            }
            hash[nums[i]] = i;
        }
        return result;
    }
};
