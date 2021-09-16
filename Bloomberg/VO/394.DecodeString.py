class Solution:
    def decodeString(self, s: str) -> str:
        num_stk = []
        cur_str = ""
        stk = []
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                tmp = i
                while tmp < len(s) and s[tmp].isdigit():
                    tmp += 1
                num_stk.append(int(s[i:tmp]))
                i = tmp
            elif ch == '[':
                #Since we have to start decoding the innermost 
                # pattern first, continue iterating over the string s, 
                # pushing each character to the stack until it is not a closing bracket ].
                #  Once we encounter the closing bracket ], 
                # we must start decoding the pattern.
                stk.append(cur_str)
                cur_str = ""
                i += 1
            elif ch == ']':
                cur_str = stk.pop() + (num_stk.pop() * cur_str)
                i += 1
            else:
                cur_str += ch
                i += 1
        return cur_str