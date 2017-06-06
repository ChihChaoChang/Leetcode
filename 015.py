'''
3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n =len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i>0 and nums[i]== nums[i-1]: continue
            L,R= i+1, n-1
            while L<R:
                temp = nums[i]+ nums[L]+nums[R]
                if temp ==0:
                    ans.append([nums[i], nums[L], nums[R]])
                    L+=1
                    R-=1
                    while L<R and nums[L]==nums[L-1]:
                        L+=1
                    while R>L and nums[R]==nums[R+1]:
                        R-=1
                elif temp <0:
                    L+=1
                else:
                    R-=1
        return ans
