class Solution:
    def wordBreak(self, s: str, wordDict):
        
        if s == "": return []
        word_set = set(wordDict)
        memo = {len(s) : ['']}
        # return the list of combinations of string s[i:]
        def dfs(i):
            if i in memo:
                return memo[i]
            memo[i] = []
            for j in range(i + 1, len(s) + 1):
                prefix = s[i:j]
                if prefix in word_set:
                    for next_s in dfs(j):
                        if next_s != '':
                            memo[i].append(prefix + ' ' + next_s)
                        else:
                            memo[i].append(prefix)
            return memo[i]
        return dfs(0)