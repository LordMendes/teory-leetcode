# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root==None):
            return root
            
        inv=TreeNode()
        inv.val=root.val
        
        if(root.left!=None):
            inv.right=self.invertTree(root.left)
        if(root.right!=None):
            inv.left=self.invertTree(root.right)
        
        return inv