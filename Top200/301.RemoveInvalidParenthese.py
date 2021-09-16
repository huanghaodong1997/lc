class Solution:
    def removeInvalidParentheses(self, s: str):
        
        min_removed = len(s)
        res_set = set()
        def backtracking(i, left_count, right_count, expr, deleted_num):
            nonlocal min_removed, res_set
            if i == len(s):
                
                if left_count == right_count:
                    if deleted_num <= min_removed: 
                        possible_expr = "".join(expr)
                        
                        if deleted_num < min_removed:
                            res_set = set()
                            min_removed = deleted_num
                        res_set.add(possible_expr)
            else:
                # for s[i] 
                # 1. if not '(', ')', just go to idx + 1
                # 2. delete the current char, deleted_num += 1
                # 3. s[i] == '(', left_count += 1
                # 4. s[i] == ')' and left_count > right_count, right_count += 1
                
                if s[i] != '(' and s[i] != ')':
                    expr.append(s[i])
                    backtracking(i + 1, left_count, right_count, expr, deleted_num)
                    expr.pop()
                else:
                    backtracking(i + 1, left_count, right_count, expr, deleted_num + 1)
                    
                    expr.append(s[i])
                    if s[i] == '(':
                        backtracking(i + 1, left_count + 1, right_count, expr, deleted_num)
                    elif s[i] == ')' and right_count < left_count:
                        backtracking(i + 1, left_count, right_count + 1, expr, deleted_num)
                    expr.pop()
        backtracking(0, 0, 0, [], 0)
        return list(res_set)
                    