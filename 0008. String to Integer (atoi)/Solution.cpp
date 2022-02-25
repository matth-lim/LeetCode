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
            if (isnegative == false && (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > INT_MAX % 10)))
                return INT_MAX;
            if (isnegative && (-result < INT_MIN / 10 || (-result == INT_MIN / 10 && -digit <= INT_MIN % 10)))
                return INT_MIN;
            result = result * 10 + digit;
            index++;
        }
        if (isnegative)
            return result * -1;
        return result;
    }
};