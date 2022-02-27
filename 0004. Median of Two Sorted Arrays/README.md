# Solution

Although this problem difficulty is hard but you can easily solve it if you merge the array. It may not be the fastest alogorithm but it works. We can merge both arrays by using the same idea as in merge sort since both arrays are already sorted we can just check both arrays if either of the array have a lower number then we add it into a new array. After it is merged we can just use simple math and get the median of the array.

Example: <br>
For odd number array: [1, 2, 3]  Median = 2<br>
For even number array: [1, 2, 3, 4] Median = 2.5 (because (2 + 3) / 2 = 2.5)

Time Complexity: **O(m + n)**\
Space Complexity: **O(m + n)**
