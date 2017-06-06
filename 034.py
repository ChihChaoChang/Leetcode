'''
Search for a Range

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        length =len(nums)
        right=length
        my_list=[]
        while left< right:
            mid = (left+right)//2
            if nums[mid]== target and( (mid ==0 or nums[mid-1]!= target)):
                my_list.append(mid)
            if nums[mid] >= target:
                right =mid
            else:
                left =mid+1
        if not my_list:
            return [-1, -1]
        right = length 
        while left< right:
            mid = (left+right)//2
            if nums[mid]== target and( (mid ==length-1 or nums[mid+1]!= target)):
                my_list.append(mid)
            
            if nums[mid] >target:
                right =mid
            else:
                left=mid+1
        return my_list
