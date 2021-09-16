class Solution:
    def evalRPN(self, tokens) -> int:
        def calculate(op1, op2, op):
            if op == '+':
                return op1 + op2
            if op == '-':
                return op1 - op2
            if op == '*':
                return op1 * op2
            if op == '/':
                return int(op1 / op2)
        
        stk = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                op2 = stk.pop()
                op1 = stk.pop()
                stk.append(calculate(op1, op2, t))
            else:
                stk.append(int(t))
        return stk[-1]