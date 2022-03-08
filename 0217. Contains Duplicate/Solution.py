class Solution:
    def containsDuplicate(self, nums):
        """
        type nums: List[int]
        rtype: bool
        """
        dic = {}
        for x in range(len(nums)):
            if nums[x] in dic:
                return True
            dic[nums[x]] = x
        return False