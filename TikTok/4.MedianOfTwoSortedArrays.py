class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        left, right = 0, m
        halfLen = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = halfLen - i
            
            # i is too small
            if i < right and nums2[j - 1] > nums1[i]:
                left = i + 1
            # i is too big
            elif i > left and nums1[i - 1] > nums2[j]:
                right = i - 1
            # i is perfect
            else:
                maxLeft = 0
                if i == 0: maxLeft = nums2[j - 1]
                elif j == 0: maxLeft = nums1[i - 1]
                else: maxLeft = maxLeft = max(nums1[i - 1], nums2[j - 1])
                
                if ((m + n) % 2 == 1): return maxLeft
                
                minRight = 0
                if i == m: minRight = nums2[j]
                elif j == n: minRight = nums1[i]
                else: minRight = min(nums1[i], nums2[j])
                
                return (maxLeft + minRight) / 2