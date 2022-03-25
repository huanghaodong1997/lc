class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        # Ensure that we always have a valid j (see below)        
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        # 
        i_min, i_max = 0, m

        # Consider m + n is odd
        # Then the left part has 1 more element then right
        half_len = (m + n + 1) // 2
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = half_len - i
            
            # Note that because length nums2 >= nums1
            # if i < m, then j - 1 must be valid, because if i == m
            # j can at most = 0, if i < m, then i > 0
            if i < m and nums1[i] < nums2[j - 1]:
                i_min = i + 1
            # j always valid
            elif i > 0 and nums1[i - 1] > nums2[j]:
                i_max = i - 1

            # other situations like i == m, then you don't need to continue searching
            # because you ocan directly get the answer
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