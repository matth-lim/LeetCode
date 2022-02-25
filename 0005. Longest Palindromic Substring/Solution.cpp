#include <string>

using std::string;

class Solution {
public:
    string longestPalindrome(string s) {
        int result_length = 0;
        int start, end;
        
        for (int i = 0; i < s.size(); i++)
        {
            int l = i;
            int r = i;
            while (l >= 0 && r < s.size() && s[l] == s[r])
            {
                if (r - l + 1 > result_length)
                {
                    start = l;
                    end = r - l + 1;
                    result_length = r - l + 1;
                }
                l--;
                r++;
            }
            l = i;
            r = i + 1;
            while (l >= 0 && r < s.size() && s[l] == s[r])
            {
                if (r - l + 1 > result_length)
                {
                    start = l;
                    end = r - l + 1;
                    result_length = r - l + 1;
                }
                l--;
                r++;
            }
        }
        return s.substr(start, end);
    }
};