class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))
# Given a list of strings, 
# you need to find the longest uncommon subsequence among them
class FollowUp:
    def findLUSlength(self, strs) -> int:
        # return True if x is a subsequence of y
        
        def isSubsequence(x, y):
            i = j = 0
            while i < len(y) and j < len(x):
                if x[j] == y[i]:
                    j += 1
                i += 1
            return j == len(x)
        res = -1
        
        for i in range(len(strs)):
            j = 0
            while j < len(strs):
                if i == j:
                    j += 1
                    continue
                # You only check the whole words because if 
                # The strs[i] is a subsequence of strs[j]
                # Then any subsequence of strs[i] is a subsequence of strs[j]
                if isSubsequence(strs[i], strs[j]):
                    break
                j += 1
            if j == len(strs):
                res = max(res, len(strs[i]))
        return res