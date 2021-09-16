#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#
# https://leetcode.com/problems/concatenated-words/description/
#
# algorithms
# Hard (36.68%)
# Likes:    883
# Dislikes: 119
# Total Accepted:    73.9K
# Total Submissions: 166.1K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# Given a list of words (without duplicates), please write a program that
# returns all concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at
# least two shorter words in the given array.
# 
# Example:
# 
# Input:
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# 
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# 
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; "ratcatdogcat"
# can be concatenated by "rat", "cat", "dog" and "cat".
# 
# 
# 
# Note:
# 
# The number of elements of the given array will not exceed 10,000 
# The length sum of elements in the given array will not exceed 600,000. 
# All the input string will only include lower case letters.
# The returned elements order does not matter. 
# 
# 
#

# @lc code=start

class TrieNode:
    def __self__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        root = TrieNode()
        for word in words:
            cur_node = root
            for ch in word:
                if ch not in cur_node.children:
                    cur_node.children[ch] = TrieNode()
                cur_node = cur_node.children[ch]
            cur_node.is_word = True
        dp = {}
        def dfs(word) -> int:
            if len(word) == 0: return -1
            if word in dp: return dp[word]
            cur_node = root
            max_res = 0
            for i, ch in enumerate(word):
                cur_node = cur_node.children[ch]
                if cur_node.is_word:
                    max_res = max(max_res, 1 + dfs(word[i+1:len(word)]))
                if max_res > 0: break
            dp[word] = max_res
            return max_res
        res = []
        for word in words:
            if dfs(word) > 0: res.append(word)

        return res

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
sol = Solution()
print(sol.findAllConcatenatedWordsInADict(words))
# @lc code=end

