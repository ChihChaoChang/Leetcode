'''
Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

'''

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        num=n
        counter=0
        while num>0 and i< n :
	        i+=1
	        num=num-i
	        counter+=1
        if num <0:
            return (i-1)
        elif num ==0:
            return (counter)
'''
Better way to do it:
	
use the formula: ( 1 + x ) x / 2 = n
and use the Quadratic formula to get: 
1/2 * x^2 + 1/2*x = n  
=> x^2 + x -2n =0
=> x= -1+ math.sqrt(1- 1* 4* (-2*n)))/2

class Solution(object):
    def arrangeCoins(self, n):
	return int(-1+ math.sqrt(1- 1* 4* (-2*n)))/2


'''
