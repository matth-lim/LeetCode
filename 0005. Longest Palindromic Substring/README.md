# Solution

To solve this problem we can loop trough the entire list and look through the element in front of it and behind of it. We need to check for both odd palindromic string and even palindromic string. We then can just return the longest palindromic string.

Ex:<br>
aba (odd)

1) take a then expand from it
2) take b then expand from it
3) take a then expand from it

abba (even)

1) take a then expand from it
2) take b then expand from it
3) take b then expand from it
4) take a then expand from it

Time Complexity: **O(n<sup>2</sup>)**\
Space Complexity: **O(1)**
