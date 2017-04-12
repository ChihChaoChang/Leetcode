'''
Convert Sorted Array to Binary Search Tree 

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
       # Definition for a binary tree node.
       length=len(nums)
       if length ==0:
          return None
       if length == 1:
          return TreeNode(nums[0])
          
       root = TreeNode(nums[length/2])
       root.left=self.sortedArrayToBST(nums[:length/2])
       root.right=self.sortedArrayToBST(nums[length/2+1:])
       return root