#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (32.41%)
# Likes:    1457
# Dislikes: 531
# Total Accepted:    209.5K
# Total Submissions: 575.8K
# Testcase Example:  '"25525511135"'
#
# Given a string s containing only digits, return all possible valid IP
# addresses that can be obtained from s. You can return them in any order.
# 
# A valid IP address consists of exactly four integers, each integer is 
# 0 and 255, separated by single dots and cannot have leading zeros. For
# example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and
# "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP
# addresses. 
# 
# 
# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:
# Input: s = "1111"
# Output: ["1.1.1.1"]
# Example 4:
# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]
# Example 5:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 3000
# s consists of digits only.
# 
# 
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1
        def dfs(prev_pos, remain_dots, cur_ip):
            if remain_dots == -1 and prev_pos == len(s) - 1:
                #update output
                output.append(cur_ip)
                return
            for cur_pos in range(prev_pos + 1, min(len(s), prev_pos + 4)):
                seg = s[prev_pos + 1: cur_pos + 1]
                if valid(seg):
                    new_ip = cur_ip
                    new_ip += seg if remain_dots == 0 else (seg + '.')
                    dfs(cur_pos, remain_dots - 1, new_ip)
        output = []
        dfs(-1,3,"")
        return output

 
            

# @lc code=end

