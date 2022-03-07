# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        type n: int
        rtype: int
        """
        l, r = 0, n
        while l <= r:
            mid = int(l + (r - l) / 2)
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                r = mid - 1
            else:
                l = mid + 1
        return 0