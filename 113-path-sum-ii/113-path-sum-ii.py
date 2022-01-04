# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        arr=[]
        def dfs(root,target,curr):
            if not root:
                return
            target=target-root.val
            if not root.right and not root.left and target==0:
                curr.append(root.val)
                arr.append(curr)
            dfs(root.left,target,curr+[root.val])
            dfs(root.right,target,curr+[root.val])
            return
        dfs(root,targetSum,[])
        return arr