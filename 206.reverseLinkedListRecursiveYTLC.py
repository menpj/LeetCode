#https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75
#Youtube based solution not ideal,iterative approach is better
#https://www.youtube.com/watch?v=G0_I-ZF0S38
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head:
            return None
        newhead=head
        if head.next:
            newhead= self.reverseList(head.next)
            head.next.next=head
        head.next=None
        return newhead
        
        