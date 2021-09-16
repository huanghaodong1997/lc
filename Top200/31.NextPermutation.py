class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1: return
        if n == 2: 
            nums[:] = nums[::-1]
            return
        cur_max = nums[n - 1]
        i = n - 2
        # We need to find the first pair of two successive numbers a[i]a[i] and a[i-1]a[i−1], from the RIGHT, which satisfy a[i] > a[i-1]a[i]>a[i−1].
        while i >= 0:
            if nums[i] < cur_max:
                break
            cur_max = max(nums[i], cur_max)
            i -= 1
            
        # We want to create the permutation just larger than the current one. Therefore, we need to replace the number a[i-1] with the number which is just larger than itself among the numbers lying to its right section, say a[j].
        if i == -1: 
            nums[:] = nums[::-1]
            return
        else:
            j = i
            m = j
            for k in range(i + 1, n):
                if nums[k] > nums[j]:
                    if nums[k] <= cur_max:
                        m = k
                    cur_max = min(cur_max, nums[k])
            # We swap the numbers a[i-1] and a[j]. We now have the correct number at index i-1
            nums[j], nums[m] = nums[m], nums[j]
            #Therefore, we simply need to reverse the numbers following a[i-1] to get the next smallest lexicographic permutation
            nums[j+1:n] =nums[j+1:n][::-1]