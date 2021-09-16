# The read4 API is already defined for you.
def read4(buf4) -> int:
    return 0

# Assume always read from start of file
class Solution:
    def read(self, buf, n) -> int:
        copied_chars = 0
        read_chars = 4
        buf4 = [''] * 4
        
        while copied_chars < n and read_chars == 4:
            read_chars = read4(buf4)
            
            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars += 1
        
        return copied_chars
#follow up, read multiple times
class Solution2:
    def __init__(self):
        self.q = []
    
    def read(self, buf, n: int) -> int:
        idx = 0
        
        while idx < n:
            if self.q:
                buf[idx] = self.q.pop(0)
                idx += 1
            else:
                buf4 = [''] * 4
                remain = read4(buf4)
                if remain == 0:
                    break
                self.q += buf4[:remain]
        return idx