'''
Palindrome Number 
Determine whether an integer is a palindrome. Do this without extra space.

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", 
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        div=1
        if x <0:
            return False
        while (x/div) >=10:
            div*=10
        while x :
            left  =x/div
            right =x%10
            if left != right:
                return False
            x=x%div
            x=x/10
            div=div/100
        return True
        
