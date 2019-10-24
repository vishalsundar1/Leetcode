# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        univalued = self.Uni_Tree(root)
        return univalued
    
    value = None
    def Uni_Tree(self, root): 
        if root is None:
            return True
        
        if self.value is None:
            self.value = root.val
            
        if (self.value != root.val):
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
