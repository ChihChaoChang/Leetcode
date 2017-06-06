'''
Add Two Numbers

ou are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #idx = ListNode(3)
        #n = idx
        #n.next = ListNode(4)
        #n = n.next
        #n.next = ListNode(5)
        #n = n.next
        #return idx
        head= ListNode(0)
        ln=head
        carry=0
        while l1 or l2 or carry:
            total, carry = carry, 0
            if l1 != None:
              total += l1.val
               l1=l1.next
            if l2 != None:
               total +=l2.val
               l2=l2.next
            if total > 9:
                carry = 1
                total -=10
            ln.next= ListNode(total)
            ln=ln.next
         return head.next
  
