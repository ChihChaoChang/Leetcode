'''
Two Sum 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n2=sorted(nums)
        left, right= 0, len(nums)-1
        list=[]
        while left< right:
            if n2[left]+n2[right]==target:
                for i in range (0,len(nums)):
                    if nums[i]== n2[left]:
                        list.append(i)
                        break
                for i in range (len(nums)-1,-1,-1):
                    if nums[i]==n2[right]:
                        list.append(i)
                        break
                break
            elif n2[left]+n2[right]< target:
                left+=1
            elif n2[left]+ n2[right] > target:
                right-=1

        list.sort()
        return (list)
