# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        a=[]
        def search(root):
            if root is None:
                return 0
            arr.append(root.val)
            search(root.left)
            search(root.right)
            return arr
        search(root)
        print(arr)
        count=[]
        for i in arr:
            count.append(arr.count(i))
        return sorted(set([arr[i] for i in range(len(arr)) if(count[i]==max(count))]))
        
        