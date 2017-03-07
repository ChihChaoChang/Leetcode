'''
Search Insert Position
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        min=nums[0]
        order=min

        i=0
        while i <= (len(nums)-1):
            if target == nums[i]:
                return (i)
            if target not in nums:
                if target < nums[i]:
		            min=target
		            return (i)
            i+=1
        return i
