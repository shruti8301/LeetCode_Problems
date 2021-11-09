# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def rootin(root):
            if not root:
                return -1
            else:
                arr.append(root.val)
                rootin(root.left)
                rootin(root.right)
                #print(arr)
                return arr
        rootin(root)
        a=set(arr)
        if len(a)==1:
            return -1
        else:
            a=list(a)
            a.sort()
            return a[1]
            #print(a[1])
        