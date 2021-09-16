class Solution:
    def countArrangement(self, N: int) -> int:
        used = set()
        count = 0
        def dfs(step):
            nonlocal count
            if step == N + 1:
                count += 1
                return
            for i in range(1, N + 1):
                if i not in used and (step % i == 0 or i % step == 0):
                    used.add(i)
                    dfs(step + 1)
                    used.remove(i)
        dfs(1)
        return count