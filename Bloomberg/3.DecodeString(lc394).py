class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        num_stk = []
        cur_str = ""
        i = 0
        while i < len(s):
            # append number to num_stk
            if s[i] >= '0' and s[i] <= '9':
                num_str = ""
                while i < len(s) and s[i] >= '0' and s[i] <= '9':
                    num_str += s[i]
                    i += 1
                num_stk.append(int(num_str))
                continue
            #push the current string into stk, reset cur_str to empty
            elif s[i] == '[':
                stk.append(cur_str)
                cur_str = ""
            # cur_str = top of the stk + top of num_stk * cur_str
            elif s[i] == ']':
                cur_str = stk.pop() + num_stk.pop() * cur_str
            else:
                cur_str += s[i]
            i += 1
        return cur_str
                
            