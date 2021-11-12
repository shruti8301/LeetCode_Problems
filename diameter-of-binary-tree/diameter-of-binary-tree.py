# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxn=0
        def tree(root):
            left=1+tree(root.left) if root.left else 0
            right=1+tree(root.right) if root.right else 0
            self.maxn=max(self.maxn,left+right)
            return max(left,right)
        
        tree(root)
        return self.maxn