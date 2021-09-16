from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode):
        self.node_list = defaultdict(list)
        
        def dfs(node, cur_row, cur_col):
            if not node: return
            self.node_list[cur_row].append((-cur_col, node.val))
            dfs(node.left, cur_row - 1, cur_col - 1)
            dfs(node.right, cur_row + 1, cur_col - 1)
        ans = []
        dfs(root, 0, 0)
        for key in sorted(self.node_list.keys()):
            tmp = [val for _, val in sorted(self.node_list[key])]
            ans.append(tmp)
        return ans

#变种 lc314: 只有在排序时改成只按照row排序即可
# class Solution:
#     def verticalOrder(self, root: TreeNode) -> List[List[int]]:
#         self.node_list = defaultdict(list)
        
#         def dfs(node, cur_row, cur_col):
#             if not node: return
#             self.node_list[(cur_row)].append((-cur_col, node.val))
#             dfs(node.left, cur_row - 1, cur_col - 1)
#             dfs(node.right, cur_row + 1, cur_col - 1)
#         ans = []
#         dfs(root, 0, 0)
#         for key in sorted(self.node_list.keys()):
#             tmp = [val for _, val in sorted(self.node_list[key], key=lambda x:x[0])]
#             ans.append(tmp)
#         return ans