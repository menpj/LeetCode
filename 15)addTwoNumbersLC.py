# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#I DEVISED THIS SOLUTION, OKAY SOLUTION
# https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150
#2. Add Two Numbers
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr=None
        carry=0
        while l1 and l2:
            
                
            a1=ListNode()

            if curr:
                curr.next=a1
            add=l1.val+l2.val+carry
            if add>=10:
                carry=1
                add=add%10
                a1.val=add
            else:
                a1.val=add
                carry=0
            if curr==None:
                head=a1
            curr=a1
            l1=l1.next
            l2=l2.next
        while l1:
            a1=ListNode()
            if curr:
                curr.next=a1
            add=l1.val+carry
            if add>=10:
                carry=1
                add=add%10
                a1.val=add
            else:
                a1.val=add
                carry=0
            if curr==None:
                head=a1
            curr=a1
            l1=l1.next
        while l2:
            a1=ListNode()
            if curr:
                curr.next=a1
            add=l2.val+carry
            if add>=10:
                carry=1
                add=add%10
                a1.val=add
            else:
                a1.val=add
                carry=0
            if curr==None:
                head=a1
            curr=a1
            l2=l2.next
        if carry==1:
            a1=ListNode(1)
            if curr:
                curr.next=a1
            

        return head       

        