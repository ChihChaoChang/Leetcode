'''
Base 7
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
'''
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        string=""
        if num<0:
            sign="-"
        else:
            sign=""
        num=abs(num)
        while num>=7:
            string+= str(num%7)
            num/=7
       
        new_string=string+str(num)
        return sign+new_string[::-1]

'''
 recurisve way:
        if num < 0:
            return str("-")+self.convertToBase7(-num)
        if num <7 :
            return str(num)
        return self.convertToBase7(num/7)+str(num%7)
       
'''
