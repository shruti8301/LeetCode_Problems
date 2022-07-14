# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # getting the index of root element for current subtree
            index = inorder.index(preorder.pop(0))    
            
            # initialises root element 
            root = TreeNode(inorder[index])
            
            # using recursion to find the next element with remaining sets of elements
            
            # elements in inorder[:index] will always be the left subtree of inorder[index]
            root.left = self.buildTree(preorder, inorder[:index])
            
            # elements in inorder[index+1:] will always be the right subtree of inorder[index]
            root.right = self.buildTree(preorder, inorder[index+1:])
            
            return root