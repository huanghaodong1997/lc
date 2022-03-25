#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#
# https://leetcode.com/problems/group-shifted-strings/description/
#
# algorithms
# Medium (60.60%)
# Likes:    951
# Dislikes: 181
# Total Accepted:    125.6K
# Total Submissions: 207.1K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# We can shift a string by shifting each of its letters to its successive
# letter.
# 
# 
# For example, "abc" can be shifted to be "bcd".
# 
# 
# We can keep shifting the string to form a sequence.
# 
# 
# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd"
# -> ... -> "xyz".
# 
# 
# Given an array of strings strings, group all strings[i] that belong to the
# same shifting sequence. You may return the answer in any order.
# 
# 
# Example 1:
# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
# Example 2:
# Input: strings = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strings.length <= 200
# 1 <= strings[i].length <= 50
# strings[i] consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # encode the strings
        
        mp = defaultdict(list)
        
        def charToId(ch):
            return ord(ch) - ord('a')
        
        def encode(s):
            base = charToId(s[0])
            res = [0]
            for i in range(1, len(s)):
                val = charToId(s[i]) - base
                if val < 0:
                    val += 26
                res.append(val)
            return tuple(res)
        for s in strings:
            key = encode(s)
            mp[key].append(s)
        
        return mp.values()
# @lc code=end

