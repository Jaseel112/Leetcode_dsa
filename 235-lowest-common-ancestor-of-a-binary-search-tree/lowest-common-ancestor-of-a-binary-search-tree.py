# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def f(root):
        #     if not root:
        #         return None
        #     if p.val<root.val and q.val<root.val:
        #         return f(root.left)
        #     elif p.val>root.val and q.val>root.val:
        #         return f(root.right)
        #     else:
        #         return root
        # return f(root)

        while(root):

            if p.val<root.val and q.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                break
        return root