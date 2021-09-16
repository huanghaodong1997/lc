from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordSet = set(wordDict)
        queue = deque()
        queue.append(0)
        visited = [False for i in range(len(s))]
        while queue:
            start = queue.popleft()
            if not visited[start]:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordSet:
                        queue.append(end)
                        if end == len(s):
                            return True
                visited[start] = True
        return False
        
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
#         @lru_cache(None)
#         def dfs(i):
#             if i == len(s): return True
#             for j in range(i + 1, len(s) + 1):
#                 if s[i:j] in wordDict:
#                     if dfs(j): return True
#             return False
#         return dfs(0)