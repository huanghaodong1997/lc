# simulation
# go from 1 to n
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        ans = "1"
        
        def helper(s):
            res = ""
            prev = s[0]
            count = 1
            for i in range(1, len(s)):
                if s[i] != prev:
                    res = res + str(count) + prev
                    prev = s[i]
                    count = 1
                else:
                    count += 1
            res = res + str(count) + prev
            return res
        
        for _ in range(2, n + 1):
            ans = helper(ans)
        return ans
        