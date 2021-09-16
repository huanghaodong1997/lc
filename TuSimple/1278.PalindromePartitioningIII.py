class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        memo = {}
        
        def moves(start, end):
            count = 0
            while start < end:
                if s[start] != s[end]: count += 1
                start += 1
                end -= 1
            return count
        
        def dp(start, end, remain):
            key = (start, end, remain)
            if key in memo:
                return memo[key]
            if (start - end + 1) == remain:
                return 0
            if remain == 1:
                memo[key] = moves(start, end)
                return memo[key]
            
            res = end - start + 1
            remain_steps = remain - 1
            for k in range(start, end - remain + 2):
                
                if (start, k, 1) not in memo:
                    memo[(start, k, 1)] = moves(start, k)
                
                cur_move = memo[(start, k, 1)]
                
                res = min(res, cur_move + dp(k + 1, end, remain_steps))
            memo[key] = res
            return res
        ans = dp(0, len(s) - 1, k)
        return ans
            