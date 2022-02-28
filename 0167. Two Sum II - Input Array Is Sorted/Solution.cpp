#include <vector>
#include <unordered_map>

using std::vector, std::unordered_map;

class Solution {
public:
    vector<int> twoSum_1(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        while (l < r)
        {
            int sum = numbers[l] + numbers[r];
            if (sum == target)
            {
                return{l + 1, r + 1};
            }
            else if (sum < target)
                l++;
            else
                r--;
        }
        return {};
    }

    vector<int> twoSum_2(vector<int>& numbers, int target) {
        for (int i = 0; i < numbers.size(); i++)
        {
            int low = 0, high = numbers.size() - 1;
            while (low <= high)
            {
                int mid = low + (high - low) / 2;
                if (target - numbers[i] == numbers[mid])
                {
                    if (i == mid)
                        low = mid + 1;
                    else
                        return {i + 1, mid + 1};
                }
                else if (target - numbers[i] < numbers[mid])
                    high = mid - 1;
                else
                    low = mid + 1;
            }
        }
        return {};
    }

    vector<int> twoSum_3(vector<int>& numbers, int target) {
        unordered_map<int, int> hash;
        for (int i = 0; i < numbers.size(); i++)
        {
            if (hash.find(target - numbers[i]) != hash.end())
            {
                return {hash[target - numbers[i]] + 1, i + 1};
            }
            else
                hash[numbers[i]] = i;
        }
        return {};
    }
};