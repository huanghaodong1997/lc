# Backtracking
class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)
        backtrack()
        return ans
# clousre number
class RecursiveSolution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return [""]
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    #always keep left is surrounded by () to avoid duplicate
                    ans.append("(" + left + ")" + right)
        return ans
# Bottom up dp
class DPSolution:
    def generateParenthesis(self, n: int):
        dp = [[""]]
        
        for i in range(1, n + 1):
            tmp = []
            for j in range(0, i):
                for left in dp[j]:
                    for right in dp[i - j - 1]:
                        tmp.append("(" + left + ")" + right)
            dp.append(tmp)
        return dp[n]