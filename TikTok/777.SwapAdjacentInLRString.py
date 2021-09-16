# check 3 contitions
# 1. start, end str without 'X' must be the same
# Accessibility
# 2. every 'L' in start must appear at the same pos or after the 'L' in target str
# 3. every 'R' in start must appear at the same pos or before the 'R' in target str

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X','') != end.replace('X', ''):
            return False
        
        t = 0
        
        for i in range(0, len(start)):
            if start[i] == 'L':
                while end[t] != 'L': t += 1
                if i < t: return False
                t += 1
        t = 0
        
        for i in range(0, len(start)):
            if start[i] == 'R':
                while end[t] != 'R': t += 1
                if i > t: return False
                t += 1
                
        return True