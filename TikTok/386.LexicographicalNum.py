class Solution:
    def lexicalOrder(self, n: int):
        ans = []
        
        def dfs(num):
            if num > n: return
            ans.append(num)
            for i in range(0, 10):
                dfs(num * 10 + i)
        for i in range(1, 10):
            dfs(i)
        return ans