# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode):
        node, output = root, []
        
        #Here the idea is to go down from the node to its predecessor, and each predecessor will be visited twice. For this go one step left if possible and then always right till the end. When we visit a leaf (node's predecessor) first time, it has a zero right child, so we update output and establish the pseudo link predecessor.right = root to mark the fact the predecessor is visited. .
        while node:

            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it and go to the right of node.
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                
                # Add current node to output, link the predecessor with thenode
                # Go to left child
                if not predecessor.right:
                    output.append(node.val)
                    # we establish this link to make sure
                    # that we have traversed the whole left subtree of current node
                    predecessor.right = node
                    node = node.left
                # When we visit the same predecessor the second time, it already points to the current node, thus we remove pseudo link and move right to the next node
                # Visited the predecessor node second times, delete the link
                else:
                    predecessor.right = None
                    node = node.right
        return output
                    
                    