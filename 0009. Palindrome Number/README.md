# Solution

We can solve this problem by flipping the second half of the integer and compare it to the first half. 

Edge cases: <br>
Number ends with 0 and it is more than 0. Eg: 10 and 01 automatically not palindrome <br>
Number less than 0. Eg: -100 automatically not palindrome

Time Complexity: **O(log(n))**\
Space Complexity: **O(1)**
