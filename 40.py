'''
Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.result=[]
        self.DFS(candidates, 0, [], target)
        return Solution.result
        
    def DFS(self, candidates, start, valuelist, target):
        length=len(candidates)
        if  target ==0  and valuelist not in Solution.result:
            return Solution.result.append(valuelist)
        
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, i+1, valuelist+ [candidates[i]], target-candidates[i])
        
