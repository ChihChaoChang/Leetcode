'''
Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(result, tmp, nums):
            if nums==[]:
                result.append(tmp)
            for i in range(len(nums)):
                helper(result, tmp+[nums[i]], nums[:i]+nums[i+1:])
            
            
        
        result=[]
        helper(result, [], sorted(nums))
        return result
