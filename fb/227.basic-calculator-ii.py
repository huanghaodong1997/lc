#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (39.88%)
# Likes:    3018
# Dislikes: 442
# Total Accepted:    320.8K
# Total Submissions: 804.2K
# Testcase Example:  '"3+2*2"'
#
# Given a string s which represents an expression, evaluate this expression and
# return its value. 
# 
# The integer division should truncate toward zero.
# 
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2^31, 2^31 - 1].
# 
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
# 
# 
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some
# number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0,
# 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.
# 
# 
#
class Solution:
    def calculate(self, s: str) -> int:
        # Time: O(n), Space: O(1)
        # Without stack, only record the last evaluated expression
        last_number = 0
        res = 0
        num_str = ""
        pre_op = "+"
        s += '+'
        
        for ch in s:
            if ch == ' ':
                continue
            elif ch.isdigit():
                num_str += ch
            else:


                if pre_op == "+" or pre_op == "-":
                    sign = 1 if pre_op == "+" else -1
                    res += last_number
                    last_number = sign * int(num_str)
                elif pre_op == '*':
                    last_number = last_number * int(num_str)
                elif pre_op == '/':
                    op1, op2 = last_number, int(num_str)
                    sign = 1 if op1 >= 0 else -1
                    last_number = abs(op1) // op2 * sign
                pre_op = ch
                num_str = ""
        return res + last_number

