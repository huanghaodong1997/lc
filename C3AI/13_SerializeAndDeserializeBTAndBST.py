class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BTCodec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, res):
            if not root:
                return res + "null,"
            res += (str(root.val)+',')
            res = rserialize(root.left, res)
            res = rserialize(root.right, res)
            return res
        return rserialize(root,"")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            if l[0] == "null":
                l.pop(0)
                return None
            node = TreeNode(int(l[0]))
            l.pop(0)
            node.left = rdeserialize(l)
            node.right = rdeserialize(l)
            return node
        l = data.split(',')
        return rdeserialize(l)


class BSTCodec:

    # Don't need to store the null Node
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def post_order(root):
            if not root: return ""
            return post_order(root.left) + post_order(root.right) + str(root.val) + ','
        return post_order(root)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        l = [int(x) for x in data.split(",") if x]
        def helper(lower, upper):
            if not l or l[-1] <= lower or l[-1] >= upper:
                return None
            root = TreeNode(l.pop())
            root.right = helper(root.val, upper)
            root.left = helper(lower, root.val)
            return root
        return helper(float('-inf'), float('inf'))