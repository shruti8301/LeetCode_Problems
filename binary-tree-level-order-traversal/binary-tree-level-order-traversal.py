# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return 
        queue=[]
        arr=[]
        queue.append(root)
        
        while(len(queue)>0):
            a=[]
            print(queue[0].val)
            for i in range (len(queue)):
                node=queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                a.append(node.val)
    
            arr.append(a)    
        return arr
            
        