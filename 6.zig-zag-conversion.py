#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return "" if s == "" else s
        direction = [1, -1]
        cur_d = 0
        cur_r = 0
        mp = defaultdict(list)
        
        for i, ch in enumerate(s):
            mp[cur_r].append(ch)
            next_r = cur_r + direction[cur_d]
            if next_r == numRows:
                cur_d = 1
                next_r = cur_r - 1
            elif next_r == -1:
                cur_d = 0
                next_r = cur_r + 1
            cur_r = next_r
        res = ""
        
        for key in range(numRows):
            if not mp[key]:
                return res
            for ch in mp[key]:
                res += ch
        return res
# @lc code=end

