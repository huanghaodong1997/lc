#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (40.72%)
# Likes:    2355
# Dislikes: 263
# Total Accepted:    266.9K
# Total Submissions: 595.1K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        for i in range(len(triangle)):
            tmp = []
            for j in range(len(triangle[i])):
                cur_num = triangle[i][j]
                dp_left = 10 ** 9 if (i - 1 < 0 or j - 1 < 0) else dp[i - 1][j - 1]
                dp_right = 10 ** 9 if (i - 1 < 0 or j >= len(dp[i - 1])) else dp[i - 1][j]
                cur_num = min(dp_left + cur_num, dp_right + cur_num, cur_num)
                tmp.append(cur_num)
            dp.append(tmp)
        return min(dp[len(triangle) - 1])
# @lc code=end

