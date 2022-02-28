class Solution:
    def removeDuplicates(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        l = 0
        for x in range(l + 1, len(nums)):
            if nums[x] != nums[l]:
                l += 1
                nums[l] = nums[x]
        return l + 1