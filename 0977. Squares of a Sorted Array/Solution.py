class Solution:
    def sortedSquares(self, nums):
        """
        type nums: List[int]
        rtype: List[int]
        """
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1,
        i = r
        while l <= r:
            if abs(nums[l]) < nums[r]:
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l += 1
            i -= 1
        return res