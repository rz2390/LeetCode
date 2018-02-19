# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        queue=[]
        line=0
        queue.append(root)
        while queue:
            level=[]
            size=len(queue)
            for i in range(size):
                node=queue.pop(0)
                if line%2==0:
                    level.append(node.val)
                else:
                    level.insert(0,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
            line+=1
        return res