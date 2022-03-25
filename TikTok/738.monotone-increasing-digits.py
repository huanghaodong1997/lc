#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (42.53%)
# Likes:    506
# Dislikes: 65
# Total Accepted:    24.6K
# Total Submissions: 54.6K
# Testcase Example:  '10'
#
# 
# Given a non-negative integer N, find the largest number that is less than or
# equal to N with monotone increasing digits.
# 
# (Recall that an integer has monotone increasing digits if and only if each
# pair of adjacent digits x and y satisfy x .)
# 
# 
# Example 1:
# 
# Input: N = 10
# Output: 9
# 
# 
# 
# Example 2:
# 
# Input: N = 1234
# Output: 1234
# 
# 
# 
# Example 3:
# 
# Input: N = 332
# Output: 299
# 
# 
# 
# Note:
# N is an integer in the range [0, 10^9].
# 
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N <= 9:
            return N
        num = [ch for ch in str(N)]
        pivot = -1
        for i in range(0, len(num) - 1):
            if num[i] > num[i + 1]:
                pivot = i
                break
        if pivot == -1: return N
        while pivot > 0 and num[pivot] == num[pivot - 1]:
            pivot -= 1
        j = pivot
        for i in range(pivot, -1, -1):
            num[i] = chr(ord(num[i]) - 1)
            if num[i] != '0':
                break
            j -= 1
        for i in range(j + 1, len(num)):
            num[i] = '9'
        if j == -1:
            return int("".join(num)[1:])
        return int("".join(num))


# @lc code=end

