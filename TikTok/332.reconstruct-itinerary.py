#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (32.52%)
# Likes:    2150
# Dislikes: 1094
# Total Accepted:    177K
# Total Submissions: 476.3K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
# 
# Note:
# 
# 
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.
# 
# 
# Example 1:
# 
# 
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# 
# 
# Example 2:
# 
# 
# Input:
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        edges = len(tickets)
        used = set()
        for src, dst in tickets:
            graph[src].append(dst)
        res_str = None
        def dfs(airport, steps, path):
            nonlocal res_str, edges
            print(graph)
            if steps == edges:
                if res_str == None:
                    res_str = path + airport
                else:
                    res_str = min(res_str, path + airport)
                return
            l = graph[airport]
            for nei in l[:]:
                if (airport, nei) in used: continue
                used.add((airport, nei))
                dfs(nei, steps + 1, path + airport + ',')
                used.remove((airport, nei))
        #airports = graph.keys()
        for key in list(graph.keys()):
            dfs(key, 0, "")
        return res_str.split(',')

sol = Solution()
input = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(sol.findItinerary(input))
print(1)
                


# @lc code=end

