#reverse preorder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        prev=[None]
        self.helper(root,prev)
        
    def helper(self,root,prev):
        if root:
            self.helper(root.right,prev)
            self.helper(root.left,prev)
            root.right=prev[0]
            root.left=None
            prev[0]=root