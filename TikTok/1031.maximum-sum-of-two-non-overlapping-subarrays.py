#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
#
# algorithms
# Medium (55.00%)
# Likes:    816
# Dislikes: 45
# Total Accepted:    29.3K
# Total Submissions: 50K
# Testcase Example:  '[0,6,5,2,2,5,1,9,4]\n1\n2'
#
# Given an array A of non-negative integers, return the maximum sum of elements
# in two non-overlapping (contiguous) subarrays, which have lengths L and M.
# (For clarification, the L-length subarray could occur before or after the
# M-length subarray.)
# 
# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1])
# + (A[j] + A[j+1] + ... + A[j+M-1]) and either:
# 
# 
# 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
# 0 <= j < j + M - 1 < i < i + L - 1 < A.length.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with
# length 2.
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with
# length 2.
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8]
# with length 3.
# 
# 
# 
# 
# Note:
# 
# 
# L >= 1
# M >= 1
# L + M <= A.length <= 1000
# 0 <= A[i] <= 1000
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        res, LMax, MMax = A[L + M - 1], A[L - 1], A[M - 1]
        for i in range(L + M, len(A)):
            LMax = max(LMax, A[i - M] - A[i - M - L])
            MMax = max(MMax, A[i - L] - A[i - M - L])
            res = max(res, LMax + A[i] - A[i - M], MMax + A[i] - A[i - L])
        return res
# @lc code=end

