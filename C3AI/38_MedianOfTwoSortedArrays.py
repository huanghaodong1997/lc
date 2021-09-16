class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        imin, imax = 0, m
        halfLen = (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = halfLen - i
            
            # i too small
            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1
            # i too big
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            # i is perfect
            else:
                # maxleft
                if i == 0: maxleft = nums2[j - 1]
                elif j == 0: maxleft = nums1[i - 1]
                else: maxleft = max(nums1[i - 1], nums2[j - 1])
                    
                if (m + n) % 2 == 1:
                    return maxleft
                if i == m: minright = nums2[j]
                elif j == n: minright = nums1[i]
                else: minright = min(nums1[i], nums2[j])
                return (maxleft + minright) / 2
# We cut A to two parts, B to two parts
# a[0] ... a[i - 1] | a[i] ... a[m - 1]
# b[0] ... b[j - 1] | b[j] ... b[n - 1]

# Ensure a property: length of left part == length of right part
# a[i - 1] must be less than or equal than b[j]
# b[j - 1] must be less than or equal than a[i]

