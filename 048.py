'''
Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length=len(matrix)
        
        for i in range(length):
            for j in range(i+1,length):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
                
        for i in range(length):
            matrix[i].reverse()
        
