# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d=defaultdict(list)
        def tree(root,depth):
            d[depth].append(root.val)
            if root.left:
                tree(root.left,depth+1)
            if root.right:
                tree(root.right,depth+1)

        tree(root,0)
        return [d[i] for i in sorted(d.keys())]
