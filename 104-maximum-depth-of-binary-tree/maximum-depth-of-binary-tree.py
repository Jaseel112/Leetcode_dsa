# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        def dfs(root):
            if not root:
                return 0
            h1=1+dfs(root.left)
            h2=1+dfs(root.right)
            return max(h1,h2)
        return dfs(root)