"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp={}

        def clone(node):
            if node in mp:
                return mp[node]
            copy=Node(node.val)
            mp[node]=copy
            for i in node.neighbors:
                copy.neighbors.append(clone(i))
            return copy
        return clone(node) if node else None
