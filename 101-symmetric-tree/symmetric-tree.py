# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(p,q):
            if not p and not q:
                return True
            if p is None or q is None:
                return False
            return p.val==q.val and mirror(p.left,q.right) and mirror(p.right,q.left)
        if not root:
            return True
        return mirror(root.left,root.right)