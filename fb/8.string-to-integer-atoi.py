#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (16.04%)
# Likes:    762
# Dislikes: 2061
# Total Accepted:    837.5K
# Total Submissions: 5.2M
# Testcase Example:  '"42"'
#
# Implement the myAtoi(string s) function, which converts a string to a 32-bit
# signed integer (similar to C/C++'s atoi function).
# 
# The algorithm for myAtoi(string s) is as follows:
# 
# 
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-'
# or '+'. Read this character in if it is either. This determines if the final
# result is negative or positive respectively. Assume the result is positive if
# neither is present.
# Read in next the characters until the next non-digit character or the end of
# the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no
# digits were read, then the integer is 0. Change the sign as necessary (from
# step 2).
# If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1],
# then clamp the integer so that it remains in the range. Specifically,
# integers less than -2^31 should be clamped to -2^31, and integers greater
# than 2^31 - 1 should be clamped to 2^31 - 1.
# Return the integer as the final result.
# 
# 
# Note:
# 
# 
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of
# the string after the digits.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "42"
# Output: 42
# Explanation: The underlined characters are what is read in, the caret is the
# current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
# ⁠        ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
# ⁠        ^
# Step 3: "42" ("42" is read in)
# ⁠          ^
# The parsed integer is 42.
# Since 42 is in the range [-2^31, 2^31 - 1], the final result is 42.
# 
# 
# Example 2:
# 
# 
# Input: s = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
# ⁠           ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
# ⁠            ^
# Step 3: "   -42" ("42" is read in)
# ⁠              ^
# The parsed integer is -42.
# Since -42 is in the range [-2^31, 2^31 - 1], the final result is -42.
# 
# 
# Example 3:
# 
# 
# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading
# whitespace)
# ⁠        ^
# Step 2: "4193 with words" (no characters read because there is neither a '-'
# nor '+')
# ⁠        ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next
# character is a non-digit)
# ⁠            ^
# The parsed integer is 4193.
# Since 4193 is in the range [-2^31, 2^31 - 1], the final result is 4193.
# 
# 
# Example 4:
# 
# 
# Input: s = "words and 987"
# Output: 0
# Explanation:
# Step 1: "words and 987" (no characters read because there is no leading
# whitespace)
# ⁠        ^
# Step 2: "words and 987" (no characters read because there is neither a '-'
# nor '+')
# ⁠        ^
# Step 3: "words and 987" (reading stops immediately because there is a
# non-digit 'w')
# ⁠        ^
# The parsed integer is 0 because no digits were read.
# Since 0 is in the range [-2^31, 2^31 - 1], the final result is 0.
# 
# 
# Example 5:
# 
# 
# Input: s = "-91283472332"
# Output: -2147483648
# Explanation:
# Step 1: "-91283472332" (no characters read because there is no leading
# whitespace)
# ⁠        ^
# Step 2: "-91283472332" ('-' is read, so the result should be negative)
# ⁠         ^
# Step 3: "-91283472332" ("91283472332" is read in)
# ⁠                    ^
# The parsed integer is -91283472332.
# Since -91283472332 is less than the lower bound of the range [-2^31, 2^31 -
# 1], the final result is clamped to -2^31 = -2147483648. 
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ',
# '+', '-', and '.'.
# 
# 
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        self.value = 0
        self.sign = 1
        cur_state = 0
        
        # DFA            (char that will make value invalid)Q-1 
        #                           |
        #.  ch come in =>  " "(Q0 cycle)  =>(0-9) Q2(0-9 cycle) => Q-2
        #                         ||-> ('+' or '-') Q1 =^(0-9)
        
        # return new state, -1 : totally invalid value should return 0, -2 : self.value != 0 or value exceed boundary, don't want to continue the loop(break)
        def DFA(ch, cur_state):
            if ch == " ":
                if cur_state == 0:
                    return 0
                return -1 if cur_state == 1 else -2
            elif (ch == '+' or ch == '-') and cur_state == 0:
                self.sign = 1 if ch == "+" else -1
                return 1
            elif ch.isdigit():
                cur_digit = ord(ch) - ord('0')
                
                if self.value > MAX // 10 or (self.value == MAX // 10 and cur_digit > 7):
                    self.value = MAX if self.sign == 1 else MIN
                    self.sign = 1
                    return -2
                    
                self.value = self.value * 10 + cur_digit
                return 2
            else:
                return -1 if cur_state == 1 or cur_state == 0 else -2

        for ch in s:
            cur_state = DFA(ch, cur_state)
            if cur_state == -1:
                return 0
            if cur_state == -2:
                break
                
        self.value *= self.sign
        return self.value

# @lc code=end

