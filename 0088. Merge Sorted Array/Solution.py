class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        type nums1: List[int]
        type m: int
        type nums2: List[int]
        type n: int
        rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp, l , r = m + n - 1, m - 1, n - 1
        while l >= 0 and r >= 0:
            if nums1[l] < nums2[r]:
                nums1[temp] = nums2[r]
                r -= 1
            else:
                nums1[temp] = nums1[l]
                l -= 1
            temp -= 1
        while l >= 0:
            nums1[temp] = nums1[l]
            temp -= 1
            l -= 1
        while r >= 0:
            nums1[temp] = nums2[r]
            temp -= 1
            r -= 1