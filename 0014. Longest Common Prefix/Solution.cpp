#include <vector>
#include <string>

using std::vector, std::string;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs){
        string res;
        for (int i = 0; i < strs[0].size(); i++)
        {
            for (int j = 1; j < strs.size(); j++)
            {
                if (strs[0][i] != strs[j][i])
                    return res;
            }
            res += strs[0][i];
        }
        return res;
    }
};