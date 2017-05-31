'''
Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m=len(num1)
        n=len(num2)
        num1=num1[::-1]
        num2=num2[::-1]
        ans=[]
        arr=[0 for i in range(m+n)]
        
        for i in range(m):
            for j in range(n):
                arr[i+j]+= int(num1[i])*int(num2[j])
        for i in range(m+n):
            digit=arr[i]%10
            carry=arr[i]/10
            if i < len(arr)-1:
                arr[i+1] += carry
            ans.insert(0, str(digit))
            
        while ans[0] == '0' and len(ans)>1:
            del ans[0]
        
        return ''.join(ans)
