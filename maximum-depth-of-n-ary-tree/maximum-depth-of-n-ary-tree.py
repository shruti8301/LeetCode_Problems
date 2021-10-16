"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        d=0
        if not root:
            return 0
        elif root.children==[]:
            return 1
        for i in root.children:
            r=1+self.maxDepth(i)
            d=max(r,d)
        return d
                
                