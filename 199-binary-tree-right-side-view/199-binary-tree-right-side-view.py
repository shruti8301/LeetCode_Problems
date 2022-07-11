# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        def postorder(root=root,level=1):
            if not root:
                return 
            if len(arr)<level:
                arr.append(root.val)
            postorder(root.right,level+1)
            postorder(root.left,level+1)
            return
        postorder()
        return arr