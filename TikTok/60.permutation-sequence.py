#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (34.08%)
# Likes:    1874
# Dislikes: 345
# Total Accepted:    211.7K
# Total Submissions: 545.1K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# Note:
# 
# 
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# 
# Example 2:
# 
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# 
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1]
        for i in range(1, 10):
            fact.append(fact[-1] * i)
        res = ""
        used = [False] * 10
        N = n
        while n:
            idx = ((k - 1) // fact[n - 1])
            k = k - (idx * fact[n - 1])
            num = 0
            for i in range(1, N + 1):
                if used[i]: continue
                if idx == 0: 
                    num = i
                    used[num] = True
                    break
                idx -= 1

            res += chr(num + ord('0'))
            n -= 1
        return res


# @lc code=end

