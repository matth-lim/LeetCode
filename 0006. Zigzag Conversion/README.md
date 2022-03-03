# Solution

This problem is definitely not my favorite but I still solved it. First know how many jumps to go to the next column the formula is (numRows - 1) * 2. Then, you still need to get the middle character, the formula for those character in the zig zag pattern is (numRows - 1) * 2 - 2 * currentRownum. After you get these two formula it should be easy to solve.

Time Complexity: **O(n)**\
Space Complexity: **O(1)**
