class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        
        
        def dfs(word, cur_str):
            if cur_str != "": words_set.add(cur_str)
            if word in words_set: return True
            
            for i in range(1, len(word)):
                prefix = word[0:i]
                
                if prefix in words_set and dfs(word[i:], cur_str + prefix):
                    return True
            return False
        words_set = set(words)
        ans = []
        for word in words:
            words_set.remove(word)
            if dfs(word, ""): ans.append(word)
            words_set.add(word)
        return ans