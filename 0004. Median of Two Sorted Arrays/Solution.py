class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        type nums1: List[int]
        type nums2: List[int]
        rtype: float
        """
        sorted_array = []
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                sorted_array.append(nums1[l])
                l += 1
            else:
                sorted_array.append(nums2[r])
                r += 1
        while l < len(nums1):
            sorted_array.append(nums1[l])
            l += 1
        while r < len(nums2):
            sorted_array.append(nums2[r])
            r += 1
        if len(sorted_array) % 2 != 0:
            return float(sorted_array[int(len(sorted_array) / 2)])
        return float((sorted_array[int(len(sorted_array) / 2 - 1)] + sorted_array[int(len(sorted_array) / 2)]) / 2)