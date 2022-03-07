# Solution

Easy math problem. Check if there are any 0 in the array because if there are 0 in the array the product will automatically be 0. Then check for the number of negative numbers. If there are odd number of negative numbers then the product will automatically be negative else the product will be positive.

Ex: <br>
[-1, 2, 3] (Odd number of negative numbers) <br>
-1 * 2 * 3 = -6

[-1, -1, 1] (Even number of negative numbers) <br>
-1 * -1 * 1 = 1

[0, 1, 1] (0 in the array) <br>
0 * 1 * 1 = 0

Time Complexity: **O(n)**\
Space Complexity: **O(1)**
