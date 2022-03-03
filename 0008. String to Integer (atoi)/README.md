# Solution

This problem is pretty easy. First you check for whitespaces then you can check for positive or negative sign, while the character is a digit use the ascii of the character to find the digit and add it to result. Check whether the number exceed the limit of INT_MAX and INT_MIN return INT_MAX or INT_MIN if exceed else return postive if postive or negative if negative.

Time Complexity: **O(n)**\
Space Complexity: **O(1)**
