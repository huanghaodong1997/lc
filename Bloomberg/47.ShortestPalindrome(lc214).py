#题目转换成找到 从头开始的最长的回文子串，这样就可以加最少的字符构成答案
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "": return s
        
        def get_next(pattern):
            n = len(pattern)
            i, j = 1, 0
            next_arr = [0] * n
            
            while i < n:
                if j == 0 and pattern[i] != pattern[j]:
                    i += 1
                elif pattern[i] == pattern[j]:
                    next_arr[i] = j + 1
                    i += 1
                    j += 1
                else:
                    j = next_arr[j - 1]
            return next_arr
        next_arr = get_next(s)
        
        j, i = 0, len(s) - 1
        
        while i > j:
            if j == 0 and s[i] != s[j]:
                i -= 1
            elif s[i] == s[j]:
                i -= 1
                j += 1
            else:
                j = next_arr[j - 1]
        pivot = i + j
        return s[pivot + 1:][::-1] + s
        