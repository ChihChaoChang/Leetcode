'''
Divide Two Integers 

 Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT. 

'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        if (dividend >0 and divisor >0) or (dividend <0 and divisor <0):
            sign =1
        else:
            sign =-1
        q=0
        dividend=abs(dividend)
        divisor =abs(divisor)
        while dividend >= divisor:
            k=0 
            tmp=divisor
            while dividend >= tmp:
                q+= 1<< k
                dividend -=tmp
                tmp <<=1
                k+=1
        if q*sign > INT_MAX :
            return INT_MAX   
        return q*sign
