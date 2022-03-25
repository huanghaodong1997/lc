#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (51.24%)
# Likes:    1691
# Dislikes: 167
# Total Accepted:    178K
# Total Submissions: 323.5K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cursor = l1
        n1 = n2 = 0
        while cursor:
            cursor = cursor.next
            n1 += 1
        cursor = l2
        while cursor:
            cursor = cursor.next
            n2 += 1
        longer = shorter = None
        if n1 >= n2:
            longer = l1
            shorter = l2
        else:
            longer = l2
            shorter = l1
            tmp = n1
            n1 = n2
            n2 = tmp
        i = longer
        j = shorter
        prev = None
        while i and j:
            num = 0
            num += i.val
            if n2 == n1:
                num += j.val
                j = j.next
                n2 -= 1
            i = i.next
            n1 -= 1
            nextNode = ListNode(num, prev)
            prev = nextNode
        carry = 0
        cursor = prev
        prev = None
        while cursor:
            num = cursor.val + carry
            if num >= 10:
                num -= 10
                carry = 1
            else:
                carry = 0
            cursor.val = num
            nextNode = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = nextNode
        return prev
            
# @lc code=end

