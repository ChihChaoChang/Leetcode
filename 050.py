'''
Pow(x, n)

Implement pow(x, n).

'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            flag= -1
        else:
            flag = 1
        
        result =1
        n=abs(n)
        
        while n >0:
            if (n&1) ==1:
                result = result *x
            n>>=1
            x*=x
        if flag <0:
            result = 1/ result
        
        return result
