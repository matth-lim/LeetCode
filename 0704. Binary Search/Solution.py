class Solution:
    def search(self, nums, target):
        """
        type nums: List[int]
        type target: int
        rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int(l + (r - l) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1