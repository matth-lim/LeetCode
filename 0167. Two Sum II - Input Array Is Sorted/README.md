# Solution 1

This algorithm uses the two pointer method. Assign one point at the start of the array and another at the end of the list. Check their sum, if lower than target then move right pointer to left else move left pointer to right.

Time Complexity: **O(n)**\
Space Complexity: **O(1)**

# Solution 2

This algorithm uses the binary search method. Use an outer loop to loop through the entire array and then find the mid point of the array and find the difference between the target and the number. If the difference equal to the mid value then return, else if smaller then mid point should move to the left side of the array, else move to the right side of the array.

Time Complexity: **O(nlog(n))**\
Space Complexity: **O(1)**

# Solution 3

This algorithm is similar to the one in [Two Sum](https://github.com/Solitudez/LeetCode/tree/main/0001.%20Two%20Sum)'s solution 2. Check it there.

Time Complexity: **O(n)**\
Space Complexity: **O(n)**
