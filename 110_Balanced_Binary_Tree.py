# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return not self.height(root)==-1
    def height(self,root):
        if not root:
            return 0
        
        l=self.height(root.left)
        r=self.height(root.right)
        
        if l==-1 or r==-1 or abs(l-r)>1:
            return -1
        return max(l,r)+1