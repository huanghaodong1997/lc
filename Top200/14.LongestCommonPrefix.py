class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # vertical scan
        if not strs: return ""
        for i in range(0, len(strs[0])):
            
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
                
                    