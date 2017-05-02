'''
Pascal's Triangle
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return 

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows<=0:
            return []
        if numRows >0:
            row = [ [] for i in range(numRows) ]
        for i in range(numRows):
            row[i]= [ 1 for j in range( i+1)]
        for i in range(numRows):
            for j in range(1,i):
                row[i][j]= row[i-1][j-1]+row[i-1][j]
        return row
