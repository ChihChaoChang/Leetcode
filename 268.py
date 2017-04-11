'''
Missing Number 


Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity? 

'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for i in nums:
            total += i
        #[0,1,3]
        alltotal=0
        for i in range(0, len(nums)+1):
            alltotal += i
        #[0,1,2,3]
        return alltotal-total
  '''
   better way to do it : use Xor
   '''
   
   
       
