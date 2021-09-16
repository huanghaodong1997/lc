class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = [-1]
        res = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stk.append(i)
            elif ch == ')':
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    res = max(res, i - stk[-1])
        return res

# O(1) Space, two scan

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         l = r = 0
#         res = 0
        
#         for ch in s:
#             if ch == '(':
#                 l += 1
#             elif ch == ')':
#                 r += 1
#             if l == r:
#                 res = max(res, l + r)
#             elif r > l:
#                 l = r = 0
#         l = r = 0
#         for ch in s[::-1]:
#             if ch == '(':
#                 l += 1
#             elif ch == ')':
#                 r += 1
#             if l == r:
#                 res = max(res, l + r)
#             elif l > r:
#                 l = r = 0
#         return res
        