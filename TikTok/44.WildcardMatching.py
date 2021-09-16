from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        @lru_cache(None)
        def backtracking(i, j):
            if i == m and j == n: return True
            if j == n: return False
            if i == m:
                return False if p[j] != '*' else backtracking(i, j+1)
            
            if p[j] == '?':
                return backtracking(i + 1, j + 1)
            elif p[j] == '*':
                res = False
                # 匹配 当前字符
                res |= backtracking(i + 1, j)
                #不匹配
                res |= backtracking(i, j+ 1)
                # 结束星号匹配
                res |= backtracking(i + 1, j + 1)
                return res
            else:
                if s[i] != p[j]:
                    return False
                else:
                    return backtracking(i + 1, j + 1)
        return backtracking(0, 0)