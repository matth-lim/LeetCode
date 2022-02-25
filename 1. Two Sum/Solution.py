class Solution:
    def twoSum_1(self, nums, target):
        """
        type nums: List[int]
        type target: int
        rtype: List[int]
        """
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]

    def twoSum_2(self, nums, target):
        """
        type nums: List[int]
        type target: int
        rtype: List[int]
        """
        map = {}
        for x in range(len(nums)):
            if target - nums[x] in map:
                return [x, map[target - nums[x]]]
            else:
                map[nums[x]] = x