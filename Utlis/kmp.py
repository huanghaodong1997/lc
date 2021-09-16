class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        word, pattern = haystack, needle
        
        def get_next(pattern):
            n = len(pattern)
            if n == 0: return []
            next_arr = [0] * n
            i, j = 1, 0
            while i < n:
                if j == 0 and pattern[i] != pattern[j]:
                    next_arr[i] = 0
                    i += 1
                elif pattern[i] == pattern[j]:
                    next_arr[i] = j + 1
                    i += 1
                    j += 1
                else:
                    j = next_arr[j - 1]
            return next_arr
        next_arr = get_next(pattern)
        n, m = len(word), len(pattern)
        i, j = 0, 0
        
        while i < n and j < m:
            if j == 0 and word[i] != pattern[j]:
                i += 1
            elif word[i] == pattern[j]:
                i += 1
                j += 1
            else:
                j = next_arr[j - 1]
        if j == m: return i - j
        return -1
#          j  
#  a a a a b
#            i    
#  a a a a a b  