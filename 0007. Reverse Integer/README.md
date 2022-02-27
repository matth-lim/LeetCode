# Solution

This question is pretty easy, to reverse the integer we can use a math trick to do it. First, get get the last digit of the number using modulus operator then cut off the last digit of the number. Multiply the digit by 10 then add the second digit. The problem also require us to make sure the reversed interger is below 2<sup>31</sup>-1 and above -2<sup>31</sup>. We can check whether the reversed integer exceed the limit before reversing the last digit. We can use the number and compare it to 214748364 and -214748364 if it exceed the limit return 0, if it is equal then check the last digit.

Example: <br>
123 get last digit (digit = 3) <br>
123 cut off last digit (becomes 12)<br>
0 * 10 + 3 become 3

12 get last digit (digit = 2) <br>
12 cut off last digit (becomes 1)<br>
3 * 10 + 2 become 32

1 get last digit (digit = 1) <br>
1 cut off last digit (becomes 0)<br>
32 * 10 + 1 become 321

(This will work for negative numbers as well)

Time Complexity: **O(n)**\
Space Complexity: **O(1)**
