#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (28.87%)
# Likes:    1654
# Dislikes: 95
# Total Accepted:    164.4K
# Total Submissions: 514.6K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, and s3, find whether s3 is formed by the interleaving of s1 and
# s2.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lower-case English letters.
# 
# 
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def helper(s1,i,s2,j,s3,k):
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if dp[i][j] >= 0: return True if dp[i][j] == 1 else False
            ans = False
            if (s1[i] == s3[k] and helper(s1, i+1, s2, j, s3, k+1)) or (s2[j] == s3[k] and helper(s1,i,s2,j+1,s3,k+1)):
                ans = True
            dp[i][j] = 1 if ans else 0
            return ans
        dp = [[-1 for i in range(len(s2))] for j in range(len(s1))]
        return helper(s1, 0, s2, 0, s3, 0)

# @lc code=end

