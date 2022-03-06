# Solution

Simple bit problem. To calculate how many 1 in a binary number we can just compare it to 1 since the binary number of 1 is 000001 then we use the & operator to compare both numbers, it will return 1 if the last digit is a 1 else it will be 0. Lastly, bit shift it to the right by 1.

Ex: <br>

00010100001 <-> 00000000001 (compare both nums with & operator)<br>
00000000001 -> 0000000000 (bit shift by 1)

Time Complexity: **O(1)**\
Space Complexity: **O(1)**
