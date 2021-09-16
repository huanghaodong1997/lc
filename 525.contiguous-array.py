#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (43.35%)
# Likes:    2426
# Dislikes: 129
# Total Accepted:    171.7K
# Total Submissions: 398.8K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1. 
# 
# 
# Example 1:
# 
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
# 
# 
# 
# Example 2:
# 
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Note:
# The length of the given binary array will not exceed 50,000.
# 
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0 : -1}
        count = 0
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                count += -1
            else:
                count += 1
            if count not in mp:
                mp[count] = i
            else:
                res = max(res, i - mp[count])
        return res

# @lc code=end

