'''

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string. 


'''
  #When n = 1, print 1
  #When n = 2, print 11
  #When n = 3, print 21
  #When n = 4, print 1211
  # ** The n starts from 1
  class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(2,n+1):
            s=self.count(s)
        return s
        
    def count(self,s):
        t=""
        count = 0
        curr = "*"
        for i in s:
            if i != curr:
                if curr != '*':
                    t += str(count)+curr
                curr = i
                count = 1
            else:
                count+=1
        t += str(count)+curr
        return t
