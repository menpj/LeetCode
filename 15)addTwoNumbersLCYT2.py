# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#best SOLUTION, youtube based
#https://www.youtube.com/watch?v=KMS0WFxrsT8
# https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150
#2. Add Two Numbers
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2:
            add=carry
            if l1:
                add+=l1.val
                l1=l1.next
            if l2:
                add+=l2.val
                l2=l2.next
            if add>=10:
                carry=1
                add=add%10   
            else:   
                carry=0
            curr.next=ListNode(add)
            curr=curr.next
        if carry==1:
            curr.next=ListNode(1)
        return dummy.next     

        