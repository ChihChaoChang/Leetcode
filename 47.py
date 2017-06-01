'''
Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(result, tmp, nums):
            if nums ==[]:
                result.append(tmp)
            else:
                for i in range(len(nums)):
                    if i>0 and nums[i]==nums[i-1]:
                        continue
                    helper(result, tmp+ [nums[i]], nums[:i]+ nums[i+1:])
        result=[]
        helper(result, [], sorted(nums))
        return result
