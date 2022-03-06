class Solution:
    def largestPerimeter(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        nums.sort()
        for x in range(len(nums) - 1, 1, -1):
            print(x)
            if nums[x - 1] + nums[x - 2] > nums[x]:
                return nums[x - 1] + nums[x - 2] + nums[x]
        return 0