class Solution:
    def canMakeArithmeticProgression(self, arr):
        """
        type arr: List[int]
        rtype: bool
        """
        arr.sort()
        diff = arr[1] - arr[0]
        for x in range(len(arr) - 1):
            if arr[x + 1] - arr[x] != diff:
                return False
        return True