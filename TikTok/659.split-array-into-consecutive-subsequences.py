#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
#
# algorithms
# Medium (41.34%)
# Likes:    1310
# Dislikes: 429
# Total Accepted:    50.8K
# Total Submissions: 115.7K
# Testcase Example:  '[1,2,3,3,4,5]'
#
# Given an array nums sorted in ascending order, return true if and only if you
# can split it into 1 or more subsequences such that each subsequence consists
# of consecutive integers and has length at least 3.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5
# 
# 
# Example 3:
# 
# 
# Input: [1,2,3,4,4,5]
# Output: False
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10000
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        tails = Counter()
        for x in nums:
            if counter[x] == 0: continue
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x + 1] += 1
            elif counter[x + 1] > 0 and counter[x + 2] > 0:
                counter[x + 1] -= 1
                counter[x + 2] -= 1
                tails[x + 3] += 1
            else:
                return False
            counter[x] -= 1
        return True

                
# @lc code=end

