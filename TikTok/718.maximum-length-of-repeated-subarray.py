#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (47.24%)
# Likes:    1529
# Dislikes: 47
# Total Accepted:    72.1K
# Total Submissions: 145K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
# 
# Example 1:
# 
# 
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)

        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(n):
            dp[0][i] = max(dp[0][i], 1 if B[i] == A[0] else 0)
        for i in range(m):
            dp[i][0] = max(dp[i][0], 1 if A[i] == B[0] else 0)
        res = 0
        for i in range(1, m):
            for j in range(1, n):
                if A[i] != B[j]: dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
        return res

# @lc code=end

