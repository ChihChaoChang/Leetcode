'''
3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, 
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        result=0
        distance = pow(2,32)-1
        for i in range(n):
            L,R = i+1, n-1
            while L<R:
                subSum = nums[i]+nums[L]+nums[R]
                diff=abs(subSum- target)
                if subSum == target:
                    return subSum
                if diff <distance:
                    result = subSum
                    distance = diff
                elif subSum > target:
                    R-=1
                else:
                    L+=1
        return result
