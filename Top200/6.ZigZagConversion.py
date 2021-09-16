from collections import defaultdict
# simulation
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return "" if s == "" else s
        direction = [1, -1]
        cur_d = 0
        cur_r = 0
        mp = defaultdict(list)
        
        for _, ch in enumerate(s):
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
# We can use min numRows, len(s))min(numRows,len(s)) lists to represent the non-empty rows of the Zig-Zag Pattern.

# Iterate through ss from left to right, appending each character to the appropriate row. The appropriate row can be tracked using two variables: the current row and the current direction.

# The current direction changes only when we moved up to the topmost row or moved down to the bottommost row.