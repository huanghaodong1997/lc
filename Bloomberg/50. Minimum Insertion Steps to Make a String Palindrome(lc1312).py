# Find maximum palindrome sub sequence, then use length of string totminus it
from functools import lru_cache
class Solution:
    def minInsertions(self, s: str) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            if i == j: return 1
            if s[i] == s[j]:
                return dp(i + 1, j - 1) + 2
            else:
                return max(dp(i + 1, j), dp(i, j - 1))
        return len(s) - dp(0, len(s) - 1)