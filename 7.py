'''
Reverse Integer 

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321 

'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        
        if x< 0:
            sign =-1
        x=sign*int(str(abs(x))[::-1])
        if abs(x) > 2147483647 :
            return 0
        else:
            return x


'''
        ans=0
        sign=1
        if x <0:
            sign=-1
        x=abs(x)
        while x >0:
            ans=ans*10+ x%10
            x/=10
            
        ans=sign*ans
        if ans  < -(1 << 31) or ans > (1 << 31) - 1:
            return 0
        return ans
'''
