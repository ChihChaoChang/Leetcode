'''
Minimum Depth of Binary Tree 

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.



'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0 
        #The tree is empty so the depth is 0 
        left =self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if left and right:
            return min(left, right)+1 
        # if both left subtree and right subtree are not empty then the min depth would be the shorter one
        return max (left, right) +1 
        # either left is None or right is None or the tree is not None but left tree and right tree are none
