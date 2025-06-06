#https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#ideal solution  by me but slightly betetr is availbale in yt
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if head:
            slow=head
        else:
            #print("retuening")
            return    
        if head.next:
            fast=head.next
        else:
            #print(retuening)
            return head
        
        tfn=fast.next
        fast.next=slow
        slow.next=None
        
        
        slow=fast
        fast=tfn
        
        while slow and fast:
            tfn=fast.next
            fast.next=slow
            slow=fast
            fast=tfn
        
        return slow
            
        