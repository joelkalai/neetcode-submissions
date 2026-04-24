# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            if left == -1 or right == -1:
                return -1 
            if abs(left - right) > 1:
                return -1 
            return max(left, right) + 1
        return True if dfs(root) != -1 else False