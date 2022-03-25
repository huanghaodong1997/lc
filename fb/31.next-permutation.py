#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (34.69%)
# Likes:    7435
# Dislikes: 2454
# Total Accepted:    612.8K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such an arrangement is not possible, it must rearrange it as the lowest
# possible order (i.e., sorted in ascending order).
# 
# The replacement must be in place and use only constant extra memory.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:
# Input: nums = [1]
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
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
        
        
# @lc code=end

