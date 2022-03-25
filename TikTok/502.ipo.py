#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#
# https://leetcode.com/problems/ipo/description/
#
# algorithms
# Hard (38.46%)
# Likes:    400
# Dislikes: 43
# Total Accepted:    19.4K
# Total Submissions: 47.6K
# Testcase Example:  '2\n0\n[1,2,3]\n[0,1,1]'
#
# 
# Suppose LeetCode will start its IPO soon. In order to sell a good price of
# its shares to Venture Capital, LeetCode would like to work on some projects
# to increase its capital before the IPO. Since it has limited resources, it
# can only finish at most k distinct projects before the IPO. Help LeetCode
# design the best way to maximize its total capital after finishing at most k
# distinct projects. 
# 
# 
# 
# You are given several projects. For each project i, it has a pure profit Pi
# and a minimum capital of Ci is needed to start the corresponding project.
# Initially, you have W capital. When you finish a project, you will obtain its
# pure profit and the profit will be added to your total capital.
# 
# 
# 
# To sum up, pick a list of at most k distinct projects from given projects to
# maximize your final capital, and output your final maximized capital.
# 
# 
# Example 1:
# 
# Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].
# 
# Output: 4
# 
# Explanation: Since your initial capital is 0, you can only start the project
# indexed 0.
# ⁠            After finishing it you will obtain profit 1 and your capital
# becomes 1.
# ⁠            With capital 1, you can either start the project indexed 1 or
# the project indexed 2.
# ⁠            Since you can choose at most 2 projects, you need to finish the
# project indexed 2 to get the maximum capital.
# ⁠            Therefore, output the final maximized capital, which is 0 + 1 +
# 3 = 4.
# 
# 
# 
# Note:
# 
# You may assume all numbers in the input are non-negative integers.
# The length of Profits array and Capital array will not exceed 50,000.
# The answer is guaranteed to fit in a 32-bit signed integer.
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        h = []
        c_p = sorted(zip(Capital, Profits))
        cur_w = W
        ans_list = W
        for c, p in c_p:
            if c <= cur_w:
                heapq.heappush(h, (-p, c))
            else:
                while h and c > cur_w:
                    (neg_p, cap) = heapq.heappop(h)
                    cur_w += abs(neg_p)
                    ans_list += abs(neg_p)
                    k -= 1
                if k == 0: break
                if c <= cur_w:
                    heapq.heappush(h, (-p, c))
                else:
                    break
        while h and k > 0:
            (neg_p, cap) = heapq.heappop(h)
            k -= 1
            ans_list += abs(neg_p)
            cur_w += abs(neg_p)
        return ans_list
        
# @lc code=end

