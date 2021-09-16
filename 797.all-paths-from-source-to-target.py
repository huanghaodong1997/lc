#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (71.43%)
# Likes:    1202
# Dislikes: 78
# Total Accepted:    92.1K
# Total Submissions: 118K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
# all possible paths from node 0 to node n - 1, and return them in any order.
# 
# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node
# graph[i][j]).
# 
# 
# Example 1:
# 
# 
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Example 2:
# 
# 
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
# 
# 
# Example 3:
# 
# 
# Input: graph = [[1],[]]
# Output: [[0,1]]
# 
# 
# Example 4:
# 
# 
# Input: graph = [[1,2,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,2,3],[0,3]]
# 
# 
# Example 5:
# 
# 
# Input: graph = [[1,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,3]]
# 
# 
# 
# Constraints:
# 
# 
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# The input graph is guaranteed to be a DAG.
# 
# 
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        graph = [set(g) for g in graph]
        res = []
        def dfs(node, path):
            if node == n - 1:
                res.append(path[:])
                return
            for n_node in graph[node]:
                path.append(n_node)
                dfs(n_node, path)
                path.pop()
        dfs(0,[0])
        return res
                

# @lc code=end

