#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (65.60%)
# Likes:    3971
# Dislikes: 178
# Total Accepted:    574.3K
# Total Submissions: 875.4K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane and an integer k, return the k closest points to the origin (0,
# 0).
# 
# The distance between two points on the X-Y plane is the Euclidean distance
# (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
# 
# You may return the answer in any order. The answer is guaranteed to be unique
# (except for the order that it is in).
# 
# 
# Example 1:
# 
# 
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just
# [[-2,2]].
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= points.length <= 10^4
# -10^4 < xi, yi < 10^4
# 
# 
#

# @lc code=start
class Solution(object):
    # Average time: O(N), Worst Case O(N^2)
    def kClosest(self, points, K):
        # quick select
        def dist(i):
            return points[i][0]**2 + points[i][1]**2

        def partion(i, j):
            # randomly pick a index as pivot
            k = randint(i, j)
            
            points[i], points[k] = points[k], points[i]
            oi = i
            pivot = dist(i)
            i += 1
            
            
            while True:
                # U always make sure that the left part of points are less or EQUAL than u
                # Because U try to get K cloest points
                # So u should not try to keep too much equal to pivot elements in the left part
                # such as [1, 2, 3, 4, 4, 4, 4, 6] and k = 4. Your goal is to get the left most 4
                while i < j and dist(i) < pivot:
                    i += 1
                
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]
            # When u get out of this loop, the j will be the final pivot point
            # Just swap j with origin i 
            points[oi], points[j] = points[j], points[oi]
            return j
        l, r = 0, len(points) - 1
        
        while l <= r:
            # Try to shrink the sorted array window to be exactly size k
            mid = partion(l, r)
            if mid == K - 1:
                break
            elif mid < K - 1:
                l = mid + 1
            else:
                r = mid - 1
        return points[:K]
            
        # Time: O(nlogk) Space: O(K)
        # h = []
        # for x, y in points:
        #     dis = x ** 2 + y ** 2
        #     heapq.heappush(h, (-dis, x, y))
        #     if len(h) > K:
        #         heapq.heappop(h)
        # return [[x, y] for _, x, y in h]
# @lc code=end

