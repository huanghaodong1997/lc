class PureDPSolution:
    def generateParenthesis(self, n: int):
        dp = [[""]]
        
        for i in range(1, n + 1):
            tmp = []
            for j in range(0, i):
                # slightly Modified version of Recursive solution
                for left in dp[j]:
                    for right in dp[i - j - 1]:
                        tmp.append("(" + left + ")" + right)
            dp.append(tmp)
        return dp[n]

# clousre number
#For each closure number c, 
# we know the starting and ending brackets
#  must be at index 0 and 2*c + 1. 
# Then, the 2*c elements between must be a valid sequence, 
# plus the rest of the elements must be a valid sequence
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