from functools import lru_cache as l
class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        
        @l(None)
        def dp(i, j):
            # if i > j:
            #     return ""
            ret = s[i:j+1]
            if j + 1 - i < 5:
                return s[i:j+1]
            ln = j+1-i
            for k in range(i, j):
                if len(dp(i, k)) + len(dp(k+1, j)) < len(ret):
                    ret = dp(i, k) + dp(k+1, j)
            
            for k in range(1, ln):
                if ln%k == 0:
                    # if pattern match the string
                    if s[i:i+k]*(ln//k) == s[i:j+1]:
                        if len(ret) > 2+len(str(ln//k))+len(dp(i, i+k-1)):
                            ret = str(ln//k)+"["+dp(i,i+k-1)+"]"
            # print(ret, s[i:j+1])
            return ret
        
        return dp(0, n-1)