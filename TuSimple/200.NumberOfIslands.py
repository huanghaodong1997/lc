class Solution:
    def numIslands(self, A) -> int:
        seen = set()
        M = len(A)
        N = len(A[0]) if M else 0
        def go(i, j):
            if i < 0 or i == M or j < 0 or j == N or A[i][j] == '0' or f'{i},{j}' in seen: # 🛑 OOB, water, or already seen 
                return 0
            seen.add(f'{i},{j}')
            for [u, v] in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]: # 🚀 DFS explore adj u,v [👆, 👉, 👇, 👈]
                go(u, v)
            return 1
        return sum(go(i, j) for i in range(M) for j in range(N))