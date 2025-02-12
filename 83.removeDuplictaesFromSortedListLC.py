# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#IDEAL SOLUTION , MADE BY ME
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow,fast=None,head
        #previous=slow
        while fast:
            if slow and slow.val==fast.val:
                slow.next=fast.next
                fast=fast.next
            else:
                slow=fast
                fast=fast.next
            '''tfn=fast.next
            fast.next=slow
            slow=fast
            fast=tfn'''
        
        #head=slow
        #self.print_list(head)
        return head