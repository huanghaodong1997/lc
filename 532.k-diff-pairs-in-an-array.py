#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#
# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
#
# algorithms
# Easy (30.31%)
# Likes:    751
# Dislikes: 1454
# Total Accepted:    121.6K
# Total Submissions: 373.3K
# Testcase Example:  '[3,1,4,1,5]\n2'
#
# Given an array of integers nums and an integer k, return the number of unique
# k-diff pairs in the array.
# 
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are
# true:
# 
# 
# 0 <= i, j < nums.length
# i != j
# a <= b
# b - a == k
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of
# unique pairs.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4)
# and (4, 5).
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# 
# 
# Example 4:
# 
# 
# Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
# Output: 2
# 
# 
# Example 5:
# 
# 
# Input: nums = [-1,-2,-3], k = 1
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^7 <= nums[i] <= 10^7
# 0 <= k <= 10^7
# 
# 
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        mp = {}
        for num in nums:
            if num not in mp:
                mp[num] = 0
            mp[num] += 1
        res = 0
        for num in nums:
            targetNum = num + k
            if targetNum != num and targetNum in mp:
                res += 1
            elif targetNum == num and mp[targetNum] > 1:
                res += 1
        return res

# @lc code=end

