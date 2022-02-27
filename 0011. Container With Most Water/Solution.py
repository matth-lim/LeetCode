class Solution:
    def maxArea(self, height):
        """
        type height: List[int]
        rtype: int
        """
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            lh = height[l]
            rh = height[r]
            max_area = max((r - l) * min(lh, rh), max_area) 
            if lh < rh:
                l += 1
            else:
                r -= 1
        return max_area