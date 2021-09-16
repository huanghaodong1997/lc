class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j, -1, -1):
                if j == i:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    dp[i][j] = True if dp[i+1][j-1] and s[i] == s[j] else False
                    
                if dp[i][j] and (j - i) > (right - left):
                    left, right = i, j
        return s[left:right+1]
# o(n^2) Space, Time complexity
# dp[i][j] mean s[i:j + 1] is a palindrome or not
# three cases:
#       if i == j -> True
#       elif i + 1 == j and s[i] == s[j]: True
#       else: dp[i + 1][j - 1] Trie amd s[i] == s[j]

# O(n^2) Time, O(1) Space 
#Expand aroung center
# There are 2n - 1 center: (1) 1 character as center (2) 2 chars as center
class ConstSpaceSolution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        start = end = 0
        
        def expand_from_center(s, l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            # r - l + 1 - 2
            return r - l - 1
                
        for i in range(len(s)):
            one_ch = expand_from_center(s, i, i)
            two_ch = expand_from_center(s, i, i + 1)
            max_len = max(one_ch, two_ch)
            
            if max_len >= end - start + 1:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end+1]
            