#include <vector>

using std::vector;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> sorted_array;
        int l = 0, r = 0;
        while(l < nums1.size() && r < nums2.size())
        {
            if (nums1[l] <= nums2[r])
            {
                sorted_array.push_back(nums1[l]);
                l++;
            }
            else
            {
                sorted_array.push_back(nums2[r]);
                r++;
            }
        }
        while (l < nums1.size())
        {
            sorted_array.push_back(nums1[l]);
            l++;
        }
        while (r < nums2.size())
        {
            sorted_array.push_back(nums2[r]);
            r++;
        }
        if (sorted_array.size() % 2 != 0)
        {
            return (double)sorted_array[sorted_array.size() / 2];
        }
        return (double)(sorted_array[(sorted_array.size() - 1) / 2] + sorted_array[sorted_array.size() / 2]) / 2.0;
    }
};