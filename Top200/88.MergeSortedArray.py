class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m - 1
        r = n - 1
        
        idx = m + n - 1
        # Begin from right to prevent overwritting
        while idx >= 0:
            if l < 0:
                nums1[idx] = nums2[r]
                r -= 1
            elif r < 0:
                nums1[idx] = nums1[l]
                l -= 1
            else:
                if nums1[l] > nums2[r]:
                    nums1[idx] = nums1[l]
                    l -= 1
                else:
                    nums1[idx] = nums2[r]
                    r -= 1
            idx -= 1
        