class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        # the node.val must be in the range of ascii
        def rserialize(root, s_list):
            if not root:
                return
            s_list.append(chr(root.val + 48))
            s_list.append(chr(len(root.children) + 48))
            for child in root.children:
                rserialize(child, s_list)
        s_list = []
        rserialize(root, s_list)
        return "".join(s_list)
        # the serialized string will look like this: chr(node.val) followed by number of children
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        idx = 0
        def rdeserialize(data):
            nonlocal idx
            if idx == len(data):
                return None
            val = ord(data[idx]) - 48
            idx += 1
            numChildren = ord(data[idx]) - 48
            root = Node(val, [])
            for i in range(numChildren):
                idx += 1
                root.children.append(rdeserialize(data))
            return root
        return rdeserialize(data)