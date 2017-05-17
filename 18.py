'''
4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        res=set()
        dict={}
        nums.sort()
                
        for i in range(n):
            for j in range(i+1,n):
                subSum=nums[i]+nums[j]
                if subSum in dict:
                    dict[subSum].append((i,j))
                else:
                    dict[subSum]=[(i,j)]
        for i in range (n):
            for j in range(i+1, n-2):
                T= target -nums[i]- nums[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0]>j:
                            res.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        
        my_list=list(res)
        return my_list
