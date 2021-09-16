from functools import lru_cache
w1, h1, v1 = 2, 2, [0, 1, 3, 4]
w2, h2, v2 = 2, 2, [0, 1, 5, 6, 10]

# dfs + memo
# Time: O(Width * Height * (height + width))
# Space: O(Width * Height)
def max_profit(width, height, values):

    @lru_cache(None)
    def dp(width, height):
        if width == 1 or height == 1:
            return values[1] * max(width, height)
        res = 0 if width !=height else values[width]

        # horizontal cut
        for i in range(1, height):
            res = max(res, dp(width, i) + dp(width, height - i))
        
        # vertical cut
        for i in range(1, width):
            res = max(res, dp(i, height) + dp(width - i, height))
        return res
    return dp(width, height)

# dp: bottom up
# dp[w][h] = max(values[w] if w == h, dp[i][height] + dp[width - i] for i in range(1, width), dp[width][i] + dp[height - i] for i in range(1, height)

def dp_max_profit(width, height, values):
    dp = [[0] * (height + 1) for _ in range(width + 1)]
    dp[1][1] = values[1]

    for i in range(1, width + 1):
        for j in range(1, height + 1):
            if i == j:
                dp[i][j] = values[i]
            for p in range(1, i):
                dp[i][j] = max(dp[i][j], dp[p][j] + dp[i - p][j])
            for q in range(1, j):
                dp[i][j] = max(dp[i][j], dp[i][q] + dp[i][j - q])
    return dp[width][height]

print(dp_max_profit(w1, h1, v1))
print(dp_max_profit(w2, h2, v2))
