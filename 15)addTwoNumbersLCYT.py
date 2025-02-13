# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#OKAY SOLUTION, betetr than mine, youtube based
# https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=wgFPrzTjm7s
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
            
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0    
            
            
            
            add=v1+v2+carry
            if add>=10:
                carry=1
                add=add%10
                
            else:
                
                carry=0
            

            curr.next=ListNode(add)
            
            curr=curr.next
            l1=l1.next if l1 else None
            
            l2=l2.next if l2 else None
                
        
        if carry==1:
            curr.next=ListNode(1)
            
            

        return dummy.next     

        