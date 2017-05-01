'''
Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt. 
Example 1:

Input: 16
Returns: True

Example 2:

Input: 14
Returns: False

'''
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=1
        while num>0:
            num-=i
            i+=2
        return num==0    
        
'''
Binary search
        left=0
        right = num
        while left<= right:
            mid=(left+right)/2
            if mid**2 == num:
                return True
            elif mid **2 > num:
                right=mid-1
            else :
                left=mid+1

        return False
        
        
Newton's Method

        x=num
        while x*x > num:
            x=(x + num/x)/2
            
        return x*x == num
'''
