#include <iostream>
#include <string>

using std::string;

class Solution {
public:
    int myAtoi(string s) {
        int index = 0;
        bool isnegative = false;
        int result = 0;
        while (s[index] == ' ')
        {
            index++;
        }
        if (s[index] == '-')
        {
            isnegative = true;
            index++;
        }
        else if (s[index] == '+')
        {
            index++;
        }
        while (index < s.size() && s[index] >= '0' && s[index] <= '9')
        {
            int digit = s[index] - '0';
            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > INT_MAX % 10))
                if (isnegative)
                    return INT_MIN;
                else
                    return INT_MAX;
            result = result * 10 + digit;
            index++;
        }
        if (isnegative)
            return result * -1;
        return result;
    }
};