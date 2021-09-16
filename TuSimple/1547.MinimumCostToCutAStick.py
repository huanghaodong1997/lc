class Solution:
    def minCost(self, n, cuts) -> int:
        cuts = sorted(cuts + [0, n])
        k = len(cuts)
        dp = [[0 for _ in range(k)] for _ in range(k)]

        for d in range(2, k):
            for j in range(d, k):
                i = j - d
                dp[i][j] = min((dp[i][m] + dp[m][j]for m in range(i + 1, j))) + cuts[j] - cuts[i]
        return dp[0][k - 1]