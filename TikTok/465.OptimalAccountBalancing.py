from collections import defaultdict
class Solution:
    def minTransfers(self, transactions) -> int:
        balance = defaultdict(int)
        for p1, p2, m in transactions:
            balance[p1] += m
            balance[p2] -= m
        money = sorted([v for _, v in balance.items() if v != 0])
        if not money: return 0
        
        def dfs(idx):
            if idx >= len(money): return 0
            if money[idx] == 0: return dfs(idx + 1)
            res = float('inf')
            for s in range(idx + 1, len(money)):
                if money[s] == 0 or (s > idx + 1 and money[s - 1] == money[s]) or money[s] * money[idx] > 0:
                    continue
                
                # clear the debt of current person
                money[s] += money[idx]
                res = min(res, 1 + dfs(idx + 1))
                money[s] -= money[idx]
            return 0 if res == float('inf') else res
        return dfs(0)
        