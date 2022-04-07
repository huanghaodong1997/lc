class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [False] * (n + 1)
        
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if s[i:j] in wordDict:
                    dp[i] |= dp[j]
        return dp[0]
        
