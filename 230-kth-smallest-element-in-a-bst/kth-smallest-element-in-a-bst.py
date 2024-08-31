# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]
        def ino(root):
            if not root:
                return
            ino(root.left)
            l.append(root.val)
            ino(root.right)
        ino(root)
        return l[k-1]