'''
Product of Array Except Self 

Given an array of n integers where n > 1, nums, 
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6]. 

'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length=len(nums)
        output=[1]*length
        left=1
        right=1
        for i in range(0,length-1):
            left*=nums[i]
            output[i+1] *=left
        for i in range(length-1,0,-1):
            right*=nums[i]
            output[i-1]*= right
        return output
