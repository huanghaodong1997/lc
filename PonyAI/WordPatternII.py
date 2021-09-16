class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        
        def backtracking(pattern, s):
            if len(pattern) == 0 and len(s) == 0: return True
            if len(pattern) == 0: return False
            
            for i in range(1, len(s) - len(pattern) + 2):
                prefix = s[:i]
                if pattern[0] not in M and prefix not in values:
                    M[pattern[0]] = prefix
                    values.add(s[:i])
                    if backtracking(pattern[1:], s[i:]):
                        return True
                    del M[pattern[0]]
                    values.remove(prefix)
                elif pattern[0] in M and M[pattern[0]] == prefix:
                    if backtracking(pattern[1:], s[i:]):
                        return True
            return False
        M = dict()
        values = set()
        return backtracking(pattern, s)