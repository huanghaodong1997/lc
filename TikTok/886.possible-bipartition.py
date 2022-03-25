#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#
# https://leetcode.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (41.41%)
# Likes:    1137
# Dislikes: 32
# Total Accepted:    64K
# Total Submissions: 143.5K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# Given a set of N people (numbered 1, 2, ..., N), we would like to split
# everyone into two groups of any size.
# 
# Each person may dislike some other people, and they should not go into the
# same group. 
# 
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the
# people numbered a and b into the same group.
# 
# Return true if and only if it is possible to split everyone into two groups
# in this way.
# 
# 
# 
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
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# 
# 
# 
# Example 2:
# 
# 
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
# 
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        group_id = [-1 for _ in range(N + 1)]
        graph = defaultdict(list)
        for src, dst in dislikes:
            graph[src].append(dst)
        visited = set()
        def dfs(i, prev_id):
            if group_id[i] == prev_id:
                return False
            if group_id != [-1]: return True
            ans = True
            cur_id = 0 if prev_id == 1 else 1
            group_id[i] = cur_id
            for adj in graph[i]:
                ans &= dfs(adj, cur_id)
            visited.add(i)
            return ans
        for i in range(1, N + 1):
            if dfs(i, 1) == False: return False

        return True
        
# @lc code=end

