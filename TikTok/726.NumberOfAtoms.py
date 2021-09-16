from collections import Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        N = len(formula)
        stk = [Counter()]
        i = 0
        
        while i < N:
            
            if formula[i] == '(':
                stk.append(Counter())
                i += 1
            elif formula[i] == ')':
                top = stk.pop()
                i += 1
                i_start = i
                while i < N and formula[i].isdigit(): i+= 1
                multi = int(formula[i_start:i]) if i > i_start else 1
                for name, v in top.items():
                    stk[-1][name] += v * multi
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower(): i += 1
                name = formula[i_start:i]
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multi = int(formula[i_start:i]) if i > i_start else 1
                stk[-1][name] += multi
        res = ""
        c = stk[-1]
        for name in sorted(c.keys()):
            res += name
            if c[name] > 1:
                res += str(c[name])
        return res