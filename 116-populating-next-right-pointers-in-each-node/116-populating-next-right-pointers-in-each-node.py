"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def two_nodes(self,left,right):
        if not left and not right:
            return 
        left.next=right
        self.two_nodes(left.left,left.right)
        self.two_nodes(left.right,right.left)
        self.two_nodes(right.left,right.right)
        
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        self.two_nodes(root.left,root.right)
        return root