# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, res):
            if not root:
                return res + ","
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
        print(data)
        def rdeserialize(l):
            if l[0] == "":
                l.pop(0)
                return None
            node = TreeNode(int(l[0]))
            l.pop(0)
            node.left = rdeserialize(l)
            node.right = rdeserialize(l)
            return node
        l = data.split(',')
        return rdeserialize(l)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))