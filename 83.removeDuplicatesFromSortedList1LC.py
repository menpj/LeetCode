# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow=head
        if head:
            fast=head.next
        else:
            return head
        #previous=slow
        while slow and fast:
            if slow.val==fast.val:
                slow.next=fast.next
                fast=fast.next
            else:
                slow=slow.next
                fast=fast.next
            '''tfn=fast.next
            fast.next=slow
            slow=fast
            fast=tfn'''
        
        #head=slow
        #self.print_list(head)
        return head
        