class Solution:
    def countOdds(self, low, high):
        """
        type low: int
        type high: int
        rtype: int
        """
        if low % 2 == 0 and high % 2 == 0:
            return int((high - low) / 2)
        else:
            return int(((high - low) / 2) + 1)