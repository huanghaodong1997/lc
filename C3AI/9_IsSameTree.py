# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

# Follow up: what about binary Tree DAG
#用 set 存 visited 过的 node ， 每次比较两个 node 前，如果它们同时在或不在 set 里才继续比较，否则直接 false


class FollowUp:
    def isSameTreeDAG(self, p: TreeNode, q: TreeNode) -> bool:
        s = set()
        def helper(p, q):
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            if p in s and q not in s or q in s and p not in s:
                return False
            s.add(p)
            s.add(q)
            return helper(p.right, q.right) and helper(p.left, q.left)
        return helper(p, q)

p1 = TreeNode(5)
p2 = TreeNode(4)
p3 = TreeNode(10)
p4 = TreeNode(4)

p1.left = p2
p1.right = p3
p3.left = p2
p2.right = p4

q1 = TreeNode(5)
q2 = TreeNode(4)
q3 = TreeNode(10)
q4 = TreeNode(4) 

q1.left = q2
q1.right = q3
q3.left = q4
q2.right = q4

f = FollowUp()
print(f.isSameTreeDAG(p1,q1))