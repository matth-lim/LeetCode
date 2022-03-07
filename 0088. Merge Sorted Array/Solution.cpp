#include <vector>

using std::vector;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int temp = m + n - 1;
        int l = m - 1;
        int r = n - 1;
        while (l >= 0 && r >= 0)
        {
            if (nums1[l] < nums2[r])
            {
                nums1[temp] = nums2[r];
                r--;
            }
            else
            {
                nums1[temp] = nums1[l];
                l--;
            }
            temp--;
        }
        while (l >= 0)
        {
            nums1[temp] = nums1[l];
            temp--;
            l--;
        }
        while (r >= 0)
        {
            nums1[temp] = nums2[r];
            temp--;
            r--;
        }
    }
};