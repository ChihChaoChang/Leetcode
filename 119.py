'''
Pascal's Triangle II 

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space? 
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r=[1]*(rowIndex+1)
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                r[i-j]+=r[i-j-1]    
        return r
        
