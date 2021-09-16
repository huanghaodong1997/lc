class Solution:
    def shortestPalindrome(self, s: str) -> str:
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
        next_arr = get_next(s)
        
        j, i = 0, len(s) - 1
        while j < i:
            if j == 0 and s[j] != s[i]:
                i -= 1
            elif s[j] == s[i]:
                j += 1
                i -= 1
            else:
                j = next_arr[j - 1]
        pivot = i + j
        return s[pivot + 1:][::-1] + s
        
        
            

# pattern= "aacecaa"
# str = "aacecaa"

# s = "aacecaa a"
# output = "aaacecaaa"

# s = "abcd"
# output "dcb a bcd"

# Time O(n ^ 2)

# kmp: Time O(n) Space O(n)
# s as pattern
#     i   ij     i + j  
# a a c e  c a   a  a

#     j
# a a a c e c aa

class ShorterSolution:
    def shortestPalindrome(self, s: str) -> str:
        new_s = s + '#' + s[::-1]
        next_arr = [0] * len(new_s)
        n = len(new_s)
        j = 0
        i = 1
        while i < n:
            if j == 0 and new_s[j] != new_s[i]:
                next_arr[i] = 0

                i += 1
            elif new_s[j] == new_s[i]:
                next_arr[i] = j + 1
                j += 1
                i += 1
            else:
                j = next_arr[j - 1]
        pivot = j - 1
        return s[pivot + 1:][::-1] + s
        
            