# O( 10 ^ len(n))
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

# O(n) Solution
class FastSolution(object):
    def lexicalOrder(self, n):
        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new //= 10
                new += 1
                while new % 10 == 0:    # deal with case like 199+1=200 when we need to restart from 2.
                    new //= 10
            ans.append(new)    
        return ans