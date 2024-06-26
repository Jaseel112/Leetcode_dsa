# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def count(root):
            if not root:
                return 0
            n=1
            n+=count(root.left)
            n+=count(root.right)
            return n
        n=count(root)
        return n
