#include <string>

using std::string;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int res = 0;
        for (int i = s.size() - 1; i >= 0; i--)
        {
            if (s[i] == ' ' && res > 0)
                return res;
            if (s[i] != ' ')
                res++;
        }
        return res;
    }
};