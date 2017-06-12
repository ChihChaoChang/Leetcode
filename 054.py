'''
Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        top =0
        left =0
        right =len(matrix[0])-1
        bottom = len (matrix)-1
        list=[]
        while left < right and top < bottom:
            for i in range(left, right):
                list.append(matrix[top][i])
            for i in range(top, bottom):
                list.append(matrix[i][right])
            for i in range(right,left,-1):
                list.append(matrix[bottom][i])
            for i in range(bottom,top,-1):
                list.append(matrix[i][left])
            left +=1
            right -=1
            top +=1
            bottom -=1
        
        if left == right and top == bottom:
            list.append(matrix[top][left])
        elif left == right:
            for i in range(top,bottom+1):
                list.append(matrix[i][left])
        elif top ==bottom:
            for i in range(left, right+1):
                list.append(matrix[top][i])
        return list
            
