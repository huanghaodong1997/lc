class Solution:
    def dfs(self, num, expression, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(expression)
            return
        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], expression + '+' + val, cur + int(val), int(val), res)
                self.dfs(num[i:], expression + '-' + val, cur - int(val), -int(val), res)
                
                # cur - last mean you have to remove the added value in the past and multiply it by curr number
                # put last * (val) as last, because when the next number is evaluation, it will take a * b as a whole expression
                self.dfs(num[i:], expression + '*' + val, cur - last + last * int(val), last * int(val), res)
    
    def addOperators(self, num, target):
        res, self.target = [], target
        
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res
        
                

# brute force, can be optimize to evaluate expression on the fly
# class Solution:
#     def addOperators(self, num: str, target: int):
#         if not num: return []
#         ans = []
#         def evaluate(expression):
#             expression += '+'
#             pre_op = '+'
#             n = len(expression)
#             i = 0
#             num_stk = []
#             num_str = ""
#             for ch in expression:
#                 if ch.isdigit():
#                     num_str += ch
#                 else:
#                     number = int(num_str)
#                     if len(str(number)) != len(num_str): return float('inf')
#                     if pre_op == '+':
#                         num_stk.append(number)
#                     elif pre_op == '-':
#                         num_stk.append(-number)
#                     elif pre_op == '*':
#                         num_stk.append(num_stk.pop() * number)
#                     pre_op = ch
#                     num_str = ""
#             return sum(num_stk)
        
#         def dfs(depth, expression):
#             if depth == len(num) - 1:
#                 expression += num[depth]
#                 val = evaluate(expression)
#                 if val == target:
#                     ans.append(expression)
#                 return
            
#             expression += num[depth]
#             dfs(depth + 1, expression)
#             dfs(depth + 1, expression + '+')
#             dfs(depth + 1, expression + '-')
#             dfs(depth + 1, expression + '*')
#         dfs(0, "")
#         return ans
                