class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        # handle even and odd case
        # if odd, make sure the leftpart has one more element than rightpart
        # so the max leftpart will be median
        halfLen = (m + n + 1) // 2
        
        # imax = m is important, because i maybe larger than the biggest index in A
        imin, imax = 0, m
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = halfLen - i
            
            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                # Getting min left
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])
                
                # left part is always one more element than right part if m + n is odd
                if (m + n) % 2 == 1:
                    return max_of_left

                # Getting min right
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2.0
# Median: dividing a set into two equal length subsets, one subsets is always greater than the other
# We cut A to two parts, B to two parts
# a[0] ... a[i - 1] | a[i] ... a[m - 1]
# b[0] ... b[j - 1] | b[j] ... b[n - 1]
# when i = 0, leftpatt of a is empty
#when i = m , rightpart of a is empty

# Ensure a property: length of left part == length of right part
# a[i - 1] must be less than or equal than b[j]
# b[j - 1] must be less than or equal than a[i]

# when i is found
# max(A[i−1],B[j−1]), when m + nm+n is odd
# max(leftpart) + min(rightpart) / 2 when m  + n is even