class Solution:
    def arraySign(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        neg = 0
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                neg += 1
        if neg % 2 == 1:
            return -1
        return 1