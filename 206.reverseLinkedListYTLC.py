# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://www.youtube.com/watch?v=G0_I-ZF0S38
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        slow,fast=None,head
        
        while fast:
            tfn=fast.next
            fast.next=slow
            slow=fast
            fast=tfn
        
        #head=slow
        #self.print_list(head)
        return slow