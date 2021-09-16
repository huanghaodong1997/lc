#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#
# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (45.15%)
# Likes:    1327
# Dislikes: 23
# Total Accepted:    34.4K
# Total Submissions: 69.2K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# Given an array A of positive integers, call a (contiguous, not necessarily
# distinct) subarray of A good if the number of different integers in that
# subarray is exactly K.
# 
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
# 
# Return the number of good subarrays of A.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2],
# [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
# 
# 
# Example 2:
# 
# 
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3],
# [2,1,3], [1,3,4].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length
# 
#

# @lc code=start
class Window:
    def __init__(self):
        self.counter = Counter()
        self.nonzero = 0
    def add(self, num):
        self.counter[num] += 1
        if self.counter[num] == 1: self.nonzero += 1
    def remove(self, num):
        self.counter[num] -= 1
        if self.counter[num] == 0: self.nonzero -= 1

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        win1 = Window()
        win2 = Window()
        ans = left1 = left2 = 0

        for end_ptr, num in enumerate(A):
            win1.add(num)
            win2.add(num)

            while win1.nonzero > K:
                win1.remove(A[left1])
                left1 += 1
            while win2.nonzero >= K:
                win2.remove(A[left2])
                left2 += 1
            ans += (left2 - left1)
        return ans

# @lc code=end

