# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            print(node.val)
            if node.val > p.val and node.val > q.val:
                return dfs(node.left)
            elif node.val < p.val and node.val < q.val:
                return dfs(node.right)
            else:
                return node
        return dfs(root)
        