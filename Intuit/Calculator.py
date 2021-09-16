s = "-1+32-3"
def calculator1(s):
    sign = 1
    res = 0
    i = 0

    while i < len(s):
        if s[i] == '+':
            sign = 1
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        else:
            tmp_i = i
            while tmp_i < len(s) and s[tmp_i].isdigit():
                tmp_i += 1
            num = int(s[i:tmp_i])
            res += sign * num
            i = tmp_i
    return res
#print(calculator1(s))
s = "(1+(4+5+2)-3)-(6+8)"
def calculator2(s):
    def update(op, num):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
    
    stack = []
    num, op = 0, '+'
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] in ['+', '-', ')']:
            update(op, num)
            if s[i] == ')':
                num = 0
                while isinstance(stack[-1], int):
                    num += stack.pop() 
                op = stack.pop()
                update(op, num)
            num, op = 0, s[i]
        elif s[i] == '(':
            stack.append(op)
            num, op = 0, '+'
    update(op, num)
    return sum(stack)
#print(calculator2(s))

s = "d-((a+b+d)+c+d)+1"
mp = {"a":1,"b":2,"c":3}
from collections import defaultdict
def calculator3(s, mp):
    def update(op, num):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
    
    stack = []
    num, op = 0, '+'
    curr_sign = 1
    sign_stk = [1]
    unused = defaultdict(int)
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] in ['+', '-', ')']:
            update(op, num)
            if s[i] == ')':
                num = 0
                curr_sign = 1
                while isinstance(stack[-1], int):
                    num += stack.pop() 
                op = stack.pop()
                update(op, num)
            num, op = 0, s[i]
        elif s[i] == '(':
            stack.append(op)
            if op == '-':
                curr_sign *= -1
            sign_stk.append(curr_sign)
            num, op = 0, '+'
        elif s[i] >= 'a' and s[i] <= 'z':
            if s[i] in mp:
                num = mp[s[i]]
            else:
                tmp = sign_stk[-1]
                if op == '-':
                    tmp *= -1
                unused[s[i]] += tmp
                    
    print(unused)
    update(op, num)
    res = str(sum(stack))
    if not unused:
        return res
    else:
        unused_ch = ""
        for ch in unused:
            freq = unused[ch]
            if freq == 0: continue
            tmp = '+' if freq >= 1 else '-'

            if abs(freq) == 1:
                tmp += ch
            else:
                tmp += "{}{}".format(abs(freq),ch)
            unused_ch += tmp
        return res + unused_ch
print(calculator3(s, mp))