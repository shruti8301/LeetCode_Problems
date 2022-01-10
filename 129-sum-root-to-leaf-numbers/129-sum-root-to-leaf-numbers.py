# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def dfs(root,result):
            result+=root.val
            if root.left==None and root.right==None:
                arr.append(result)
                return
            if root.left:
                dfs(root.left,result*10)
            if root.right:
                dfs(root.right,result*10)
        if root:
            dfs(root,0)
            return sum(arr)
        return
            