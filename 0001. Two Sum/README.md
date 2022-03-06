# Solution 1

This algorithm uses the brute-force method to solve the problem by using two loops.
The first loop check for the first number the entire list, the second loop check for the numbers after the first number.
If the first number adds the second number equal to the target value then return the the index of both numbers.

Time Complexity: **O(n<sup>2</sup>)**\
Space Complexity: **O(1)**


# Solution 2

This algorithm uses a hashtable to solve the problem.
We can know the one of the number by using the target value minus a number in the list

ex: 7 + 5 = 12 | 12 - 7 = 5

If we found a match in the hashtable then we can return the index of both numbers else we add the current number into the hashtable. 
We only need to loop through the entire list once.

Time Complexity: **O(n)**\
Space Complexity: **O(n)**

test



